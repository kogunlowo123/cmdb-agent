# CMDB Agent Architecture

Configuration Management Database agent that maintains accurate CI records, maps service dependencies, detects configuration drift, reconciles discovered vs documented infrastructure, and supports change impact analysis.

## Domain Tools

- **query_cmdb**: Query CMDB for configuration items matching criteria
- **map_dependencies**: Map upstream and downstream dependencies for a service
- **detect_drift**: Detect configuration drift between CMDB records and actual state
- **reconcile_inventory**: Reconcile discovered infrastructure with CMDB records
- **analyze_change_impact**: Analyze impact of a proposed change on dependent services