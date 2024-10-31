FROM python:3.12-slim as builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1
    
WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.path --unset
RUN poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./

RUN poetry install

FROM builder as final

COPY --from=builder app/.venv app/.venv

WORKDIR /app

COPY . .

RUN poetry install

CMD ["poetry", "run", "start_app"]

EXPOSE 8000