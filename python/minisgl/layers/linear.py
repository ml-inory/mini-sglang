"""Teaching scaffold for minisgl.layers.linear.

Scaffold for minisgl.layers.linear.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class _LinearTPImpl:
    """Real implementation of a linear layer with tensor parallelism."""

    def __init__(
        self, full_isize: int, full_osize: int, local_isize: int, local_osize: int, has_bias: bool
    ):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class LinearReplicated:
    """Linear layer where weights are replicated (not sharded) across all TP ranks.
    Each GPU holds the full weight matrix.
    """

    def __init__(self, input_size: int, output_size: int, has_bias: bool):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")


class LinearColParallelMerged:
    """TODO: implement `LinearColParallelMerged`. (original base: _LinearTPImpl)"""

    def __init__(self, input_size: int, output_sizes: List[int], has_bias: bool):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")


class LinearQKVMerged:
    """TODO: implement `LinearQKVMerged`. (original base: _LinearTPImpl)"""

    def __init__(
        self, hidden_size: int, head_dim: int, num_qo_heads: int, num_kv_heads: int, has_bias: bool
    ):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")


class LinearOProj:
    """TODO: implement `LinearOProj`. (original base: _LinearTPImpl)"""

    def __init__(self, input_size: int, output_size: int, has_bias: bool):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class LinearRowParallel:
    """TODO: implement `LinearRowParallel`. (original base: _LinearTPImpl)"""

    def __init__(self, input_size: int, output_size: int, has_bias: bool):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")
