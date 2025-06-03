#!/bin/bash

# Wait for the database to be ready
sleep 10

set -e

# Initialize the Superset database
pip install --no-cache-dir sqlalchemy-dremio pyarrow sqlalchemy-utils

# Initialize the database
superset db upgrade

# Create an admin user
superset fab create-admin \
    --username admin \
    --firstname Admin \
    --lastname User \
    --email admin@example.com \
    --password admin

# Initialize Superset
superset init

# Register Dremio DB via Python script
python register_dremio.py

# Start the Superset server
superset run -h 0.0.0.0 -p 8088