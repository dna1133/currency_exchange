.PHONY: all

DC = docker compose
# STORAGES=docker-compose/storages.yaml
ENV = --env-file .env

app:
	poetry run start_app

up_storages:
	${DC} ${ENV} -f ${STORAGES} up -d --build

down_storages:
	${DC} ${ENV} -f ${STORAGES} down