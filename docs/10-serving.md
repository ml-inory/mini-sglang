# 10 服务链路：HTTP、Token 与流式回复

服务层的目标是把 OpenAI 风格的文本接口转换成内部 token 请求，再把离散 token 安全地还原成文本。

## 本章作业 H10

实现 server、tokenizer、detokenizer、LLM 门面和 shell。交付 `/v1/models`、chat completion 的 stream/non-stream、UTF-8 增量解码和客户端断开 abort 测试。

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_server.py -q
```

## 进程角色

### API Server

负责：

- HTTP 路由与请求校验；
- 分配 uid；
- 选择 prompt template；
- 发起 tokenize 请求；
- 把生成结果映射成 OpenAI response 或 SSE stream；
- 客户端断开时发送 abort。

### Tokenizer Worker

负责 tokenizer 生命周期、文本编码和特殊 token 处理。不要把 tokenizer 复制到每个 scheduler 循环中。

### Detokenizer Worker

负责增量解码。一个 token 的字节边界可能不完整，尤其 UTF-8 多字节字符会跨越多个 token。实现时需要使用增量 decoder，而不是每个 token 单独 `decode`。

### Scheduler

只处理 token id、采样参数和生命周期，不应依赖 HTTP 框架。

### LLM 客户端封装

`llm/llm.py` 提供面向 Python 的简单接口，内部可走本地进程或在线 API。先保持接口稳定，再选择传输实现。

## 请求流程

```text
HTTP prompt
  -> validate
  -> tokenize
  -> scheduler prefill/decode
  -> detokenize incrementally
  -> stream chunks or aggregate final response
```

非流式响应只是收集完所有 chunk 再构造一次响应。不能为了非流式复制一套调度逻辑。

## OpenAI 兼容契约

至少需要定义：

- `/v1/models`；
- `/v1/chat/completions`；
- stream 与 non-stream；
- role、content、finish_reason；
- usage token 计数；
- request id；
- 常见错误码。

先使用固定响应测试 schema，再接真实模型。测试不要依赖特定模型生成文本。

## 流式状态

流式路径中可能出现：

- 生成多个 token 才形成一个可显示文本 chunk；
- 客户端在首个 token 前断开；
- detokenizer 队列暂时为空；
- scheduler 已结束但最终文本尚未 flush；
- 多个请求共享同一连接或同一 upstream stream。

为每个 uid 维护明确的 closed/aborted/finished 状态。任何 `yield` 之后的 `finally` 都应负责取消订阅和释放请求。

## Chat Template

不同模型需要不同 chat template。模板属于模型/tokenizer 配置，不应硬编码在 API handler。测试应使用固定消息列表输出固定 token 序列，避免把自然语言生成当成模板单元测试。

## Shell 与 Benchmark Client

- `shell.py`：交互模式，维护聊天历史，支持 reset；
- `benchmark/client.py`：测量 TTFT、ITL、总延迟和吞吐；
- `benchmark/perf.py`：GPU event/timing 辅助。

benchmark client 必须区分“服务端处理时间”和“网络排队时间”，并记录并发度、输入/输出长度分布。

## 安全与健壮性

- 限制 prompt 和输出长度；
- 校验 temperature、top-p、top-k；
- 不把异常 traceback 原样返回公网；
- 不在日志里输出完整隐私 prompt；
- 对 uid 和 active request 做容量限制；
- 对慢客户端设置背压；
- 确保 abort 幂等。

## 本章验收

- 无模型时 `/v1/models` 和 schema 测试通过；
- tokenizer 特殊 token round-trip 通过；
- UTF-8 增量 detokenize 通过；
- stream=true 产生合法 SSE；
- stream=false 返回完整 response；
- 客户端断开触发 abort；
- 请求结束后 active/缓存/table slot 都归零；
- `test_server.py` 通过。

下一章：[性能实验](11-performance.md)。
