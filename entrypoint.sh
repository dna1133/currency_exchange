#!/bin/bash

set -e 

echo "Applying migrations..."
poetry run alembic upgrade head

echo "Starting the application..."
poetry run start_app

exec "$@" 
