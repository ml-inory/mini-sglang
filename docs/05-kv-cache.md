# 05 KV Cache 与前缀复用

KV Cache 是本项目从“逐 token 重算”升级为“连续生成服务”的第一道关键优化。

## 本章作业 H05

依次实现 cache 基础契约、Naive 前缀缓存、Radix Tree、MHA pool 和 `scheduler/cache.py`。必须补齐 page size 为 `1/2/4`、共享前缀、分叉、lock 和 evict 的测试。

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_cache.py -q
```

提交物包含测试结果、一次容量估算和资源不变量清单。

## 为什么缓存 K/V

自回归生成时，历史 token 的 Key 和 Value 不会因新 token 改变。把每层的 K、V 留下来，decode 只需为最新 token 计算 Q、K、V，并让新 Q attend 历史 K/V。

单层缓存容量近似为：

```text
2 * num_tokens * num_kv_heads * head_dim * element_size
```

整模型再乘以层数。练习：对 `num_layers=28, num_kv_heads=8, head_dim=128, dtype=fp16, tokens=8192` 估算单请求容量。再思考 batch 与分页 overhead。

## 两种缓存

### 数据缓存：K/V tensor pool

`MHAKVCache` 的职责是按 layer 和物理 slot 读取/写入 K、V。它不应该理解“请求”或“Radix Tree”，只暴露物理存储能力。

需要确认：

- layout 是 `[layer, slot, head, dim]` 还是其他形式；
- 读写是否要求连续；
- CPU/GPU 设备一致；
- dtype 是否由模型配置统一决定；
- `store_kv` 的位置索引是 token 级还是 page 级。

### 元数据缓存：前缀索引

`NaivePrefixCache` 用简单方法保存“token 序列 -> 物理位置”，适合先打通正确性。

`RadixPrefixCache` 用压缩前缀树复用共享前缀。一个节点通常保存：

- 一段连续 token key；
- 对应的物理 KV indices；
- 子节点；
- 引用计数；
- 最近访问时间戳。

节点 key 不需要每个 token 一个节点；压缩边可以减少树规模和遍历成本。

## 匹配流程

匹配 prefix 时，目标是找到最长、可安全复用的已有序列：

1. 从 root 开始；
2. 用输入序列剩余部分定位子节点；
3. 比较节点 key 与剩余输入；
4. 完整匹配则继续向下；
5. 部分匹配则拆分节点；
6. 返回聚合后的物理 indices。

返回值必须区分“节点身份”和“当前请求命中长度”。不能只返回一个长度，因为后续 lock、insert 和 evict 都需要节点。

## 插入流程

插入时可能遇到三种情况：

1. 完全命中已有路径；
2. 命中一段后新增分支；
3. 在节点中间产生分歧，需要 split。

同时要处理尾部不足一个 page 的部分。常见策略是只缓存完整的 page 对齐前缀，尾部留给当前请求，避免以后无法按页安全复用。

## 引用计数与淘汰

一个 cache handle 在被某个请求使用期间必须 locked，不能淘汰。引用计数通常沿节点到 root 的路径维护，否则淘汰祖先时会破坏所有后代。

淘汰建议使用最近最少使用或按时间戳的堆。实现时要回答：

- 只淘汰叶子吗？
- 叶子淘汰后父节点什么时候成为叶子？
- protected/evictable 大小何时变化？
- 目标释放量刚好跨节点时，是否允许过量淘汰？
- `evict(0)` 是否幂等？

## Page table 与空闲页池

`CacheManager` 连接 prefix cache、free page 和请求 page table。

关键不变量：

- free slots 中每一项是 page 起点；
- 分配后从 free list 移除；
- page table 记录 token 到物理位置的映射；
- 释放时只把完整 page 放回；
- 活跃 handle 引用的 page 不可淘汰；
- 所有释放完成后，free pages + cached pages = total pages。

先实现 page_size=1，再测试 2、4、8。跨页错误通常只在 `page_size > 1` 时暴露。

## 推荐实现里程碑

1. `SizeInfo` 的总量派生；
2. 不做复用的 Naive cache；
3. Radix 节点查找与完整匹配；
4. 节点 split；
5. insert 分支；
6. lock/unlock；
7. 基于引用计数与时间戳的 evict；
8. CacheManager 分配、写入 page table、释放；
9. integrity check；
10. 随机操作序列测试和压力测试。

## 必测边界

- 空序列；
- 长度为 1；
- 恰好一页；
- 比一页多一个 token；
- 两个请求共享一整段前缀；
- 一个请求共享后分叉；
- 请求仍持有 handle 时触发淘汰；
- 重复 unlock 或重复 free；
- 分配需求大于总可释放容量。

测试入口：`tests/exercises/test_cache.py`，并建议新增 `tests/exercises/test_cache_properties.py` 做随机模型测试。

下一章：[调度器](06-scheduler.md)。
