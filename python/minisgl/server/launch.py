"""Teaching scaffold for minisgl.server.launch.

Scaffold for minisgl.server.launch.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _run_scheduler(args: ServerArgs, ack_queue: mp.Queue[str]) -> None:
    """TODO: implement `_run_scheduler`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _run_scheduler()")


def launch_server(run_shell: bool = False) -> None:
    """TODO: implement `launch_server`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement launch_server()")
