from currency_exchange.core.configs import settings


def start_app():
    import uvicorn

    uvicorn.run(
        app="src.currency_exchange.app.app_server:app",
        host=settings.APPLICATION_HOST,
        port=settings.APPLICATION_PORT,
        reload=True,
        workers=settings.APPLICATION_WORKERS,
    )


if __name__ == "__main__":
    start_app()
