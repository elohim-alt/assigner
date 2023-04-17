#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: ./scripts/setup_and_run.sh <drivers_file> <shipments_file>"
  exit 1
fi

# Navigate to the project root
cd "$(dirname "$0")/.."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the assignment optimizer
python -m assigner "$1" "$2"

# Deactivate the virtual environment
deactivate
