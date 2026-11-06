from __future__ import annotations

from dataclasses import dataclass

import pytest

pytestmark = pytest.mark.exercise


@dataclass(eq=False)
class DummyRequest:
    uid: int
    can_decode: bool = True


def test_table_slots_are_allocated_once_and_reused() -> None:
    torch = pytest.importorskip("torch")
    from minisgl.scheduler.table import TableManager

    table = TableManager(3, torch.zeros((3, 8), dtype=torch.int32))
    slots = {table.allocate(), table.allocate(), table.allocate()}
    assert slots == {0, 1, 2}
    assert table.available_size == 0
    table.free(1)
    assert table.available_size == 1
    assert table.allocate() == 1


def test_decode_manager_orders_requests_and_drops_finished_ones() -> None:
    from minisgl.core import Batch
    from minisgl.scheduler.decode import DecodeManager

    alive_late = DummyRequest(uid=9)
    alive_early = DummyRequest(uid=2)
    finished = DummyRequest(uid=5, can_decode=False)
    manager = DecodeManager(page_size=4)
    manager.filter_reqs([alive_late, alive_early, finished])
    batch = manager.schedule_next_batch()
    assert isinstance(batch, Batch)
    assert [request.uid for request in batch.reqs] == [2, 9]
