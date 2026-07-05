"""CMDB Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_query_cmdb():
    """Test Query CMDB for configuration items matching criteria."""
    tools = AgentTools()
    result = await tools.query_cmdb(ci_type="test", filters="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_map_dependencies():
    """Test Map upstream and downstream dependencies for a service."""
    tools = AgentTools()
    result = await tools.map_dependencies(service_name="test", depth=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_drift():
    """Test Detect configuration drift between CMDB records and actual state."""
    tools = AgentTools()
    result = await tools.detect_drift(ci_id="test", comparison_source="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_reconcile_inventory():
    """Test Reconcile discovered infrastructure with CMDB records."""
    tools = AgentTools()
    result = await tools.reconcile_inventory(discovery_source="test", scope="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.cmdb_agent_agent import CmdbAgentAgent
    agent = CmdbAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
