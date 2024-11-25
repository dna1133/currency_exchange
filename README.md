# Currence-exchange
Example REST API project.
Stack:
  - FastAPI
  - Postgres
  - Redis
  - Migrations (alembic)

## Structure
fastapi-project
├── src
│   ├── project_name
│   │   ├── api    # API entrypoints
│   │   ├── app    # Application 
│   │   ├── core   # Configs, DI_conteiner 
│   │   ├── domain 
│   │   ├── gateways  # Outter layer
│   │   ├── logs
│   │   ├── services  # app services 
│   │   └── main.py   # entrypoint
│   └── frontend
├── tests/
├── .env
├── .gitignore
├── pyproject.toml
├── alembic.ini
├── Makefile
├── Dockerfile
├── docker-compose.yaml
└── README.MD

### Start project
```sh
docker compose --env-file .env up --build
```


# Currence-exchange
Проект представляет собой REST API, который обеспечивает работу с данными о валютах и обменных курсах. Пользователи могут просматривать и редактировать данные о валютах, а также проводить расчет конвертации различных сумм между различными валютами.

## Архитектура проеката
Проект разработан с применением принципов из Чистой Архитектуры.
И разделен на следующие слои:
  - api - REST API для взаимодействия с сервером.
  - app - сценарии использования приложения.
  - core - настройки, конфиги, взаимодействия с фреймворком и тд. Критичные данные, которые не влияют на бизнес-процессы, но необходимы для работы приложения с текущим стеком.
  - gateways - база данных.
  - services - сервисы для соединения внешнего слоя (базы данных и кэш) с бизнес-логикой.
  - frontend - простенький фронтэнд для примера отображения данных полученных через API.
  - main - слой собирающий вместе всё приложение.

### Запуск проеката
1. Makefile
```sh
make up
```

2. DC
```sh
docker compose --env-file .env up --build
```
