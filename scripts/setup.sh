#!/bin/bash

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

# Deactivate the virtual environment
deactivate
