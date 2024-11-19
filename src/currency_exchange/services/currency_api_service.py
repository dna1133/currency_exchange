from currency_exchange.domain.entity.currency import Currency

# from currency_exchange.gateways.database.postgresql.database import Database


class CurrencyService:
    async def get_one(
        self,
        currency: str,
    ) -> Currency:
        # async with db.get_read_only_session() as session:
        ...
