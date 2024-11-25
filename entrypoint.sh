#!/bin/bash

set -e 

if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "example.env скопирован в .env"
fi

echo "Applying migrations..."
poetry run alembic upgrade head

echo "Starting the application..."
poetry run start_app

exec "$@" 
