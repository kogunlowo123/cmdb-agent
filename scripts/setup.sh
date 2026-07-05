#!/bin/bash
set -euo pipefail
echo "Setting up CMDB Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
