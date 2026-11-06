from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pytest

pytestmark = pytest.mark.exercise


@dataclass
class Payload:
    count: int
    text: str
    nested: list[Any]


def test_nested_dataclass_round_trip() -> None:
    from minisgl.message.utils import deserialize_type, serialize_type

    original = Payload(count=2, text="hello", nested=[1, True, "x"])
    encoded = serialize_type(original)
    decoded = deserialize_type({"Payload": Payload}, encoded)
    assert decoded == original
