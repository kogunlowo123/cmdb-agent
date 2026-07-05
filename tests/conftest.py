"""Test configuration for CMDB Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "cmdb-agent", "category": "IT Operations"}
