.PHONY: all

DC = docker compose
# STORAGES=docker-compose/storages.yaml
ENV = --env-file .env
DC = docker compose
ENV = --env-file .env

app:
	poetry run start_app

d_up:
	${DC} ${ENV} up --build