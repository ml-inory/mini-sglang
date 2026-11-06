from __future__ import annotations

import pytest

pytestmark = [pytest.mark.exercise, pytest.mark.integration]
pytest.importorskip("fastapi")


def test_openai_model_list_contract() -> None:
    from fastapi.testclient import TestClient

    from minisgl.server.api_server import create_app

    response = TestClient(create_app()).get("/v1/models")
    assert response.status_code == 200
    assert "data" in response.json()
