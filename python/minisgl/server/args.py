"""Teaching scaffold for minisgl.server.args.

Scaffold for minisgl.server.args.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class ServerArgs:
    """TODO: implement `ServerArgs`. (original base: SchedulerConfig)"""

    @property
    def share_tokenizer(self) -> bool:
        """TODO: implement `share_tokenizer`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement share_tokenizer()")

    @property
    def zmq_frontend_addr(self) -> str:
        """TODO: implement `zmq_frontend_addr`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement zmq_frontend_addr()")

    @property
    def zmq_tokenizer_addr(self) -> str:
        """TODO: implement `zmq_tokenizer_addr`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement zmq_tokenizer_addr()")

    @property
    def tokenizer_create_addr(self) -> bool:
        """TODO: implement `tokenizer_create_addr`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement tokenizer_create_addr()")

    @property
    def backend_create_detokenizer_link(self) -> bool:
        """TODO: implement `backend_create_detokenizer_link`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement backend_create_detokenizer_link()")

    @property
    def frontend_create_tokenizer_link(self) -> bool:
        """TODO: implement `frontend_create_tokenizer_link`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement frontend_create_tokenizer_link()")

    @property
    def distributed_addr(self) -> str:
        """TODO: implement `distributed_addr`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement distributed_addr()")


def parse_args(args: List[str], run_shell: bool = False) -> Tuple[ServerArgs, bool]:
    """Parse command line arguments and return an EngineConfig.

    Args:
        args: Command line arguments (e.g., sys.argv[1:])

    Returns:
        EngineConfig instance with parsed arguments
    """
    raise NotImplementedError("Teaching scaffold: implement parse_args()")
