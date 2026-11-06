"""Teaching scaffold for minisgl.kernel.moe_impl.

Scaffold for minisgl.kernel.moe_impl.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def fused_moe_kernel_triton(
    A: torch.Tensor,
    B: torch.Tensor,
    C: torch.Tensor,
    topk_weights: torch.Tensor,
    topk_ids: torch.Tensor,
    sorted_token_ids: torch.Tensor,
    expert_ids: torch.Tensor,
    num_tokens_post_padded: torch.Tensor,
    mul_routed_weight: bool,
    top_k: int,
    config: Dict[str, Any],
    compute_type: torch.dtype,
) -> None:
    """TODO: implement `fused_moe_kernel_triton`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement fused_moe_kernel_triton()")


def moe_sum_reduce_triton(input: torch.Tensor, output: torch.Tensor) -> None:
    """TODO: implement `moe_sum_reduce_triton`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement moe_sum_reduce_triton()")
