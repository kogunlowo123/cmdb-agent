# CMDB Agent

[![CI](https://github.com/kogunlowo123/cmdb-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/cmdb-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: IT Operations | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Configuration Management Database agent that maintains accurate CI records, maps service dependencies, detects configuration drift, reconciles discovered vs documented infrastructure, and supports change impact analysis.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `query_cmdb` | Query CMDB for configuration items matching criteria |
| `map_dependencies` | Map upstream and downstream dependencies for a service |
| `detect_drift` | Detect configuration drift between CMDB records and actual state |
| `reconcile_inventory` | Reconcile discovered infrastructure with CMDB records |
| `analyze_change_impact` | Analyze impact of a proposed change on dependent services |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/cmdb/query` | Query CMDB |
| `GET` | `/api/v1/cmdb/dependencies` | Map dependencies |
| `POST` | `/api/v1/cmdb/drift` | Detect drift |
| `POST` | `/api/v1/cmdb/reconcile` | Reconcile inventory |
| `POST` | `/api/v1/cmdb/change-impact` | Analyze change impact |

## Features

- Ci Management
- Dependency Mapping
- Drift Detection
- Reconciliation
- Change Impact

## Integrations

- Servicenow Cmdb
- Device42
- Infoblox
- Aws Config
- Azure Resource Graph

## Architecture

```
cmdb-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── cmdb_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ServiceNow CMDB + Discovery + Change Management**

---

Built as part of the Enterprise AI Agent Platform.
