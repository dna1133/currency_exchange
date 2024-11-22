from sqlalchemy import Column, String, DECIMAL, ForeignKey
from currency_exchange.gateways.database.models.base import Base


class ExchangeRates(Base):
    __tablename__ = "ExchangeRates"

    oid = Column(String, primary_key=True, unique=True)
    base_currency_oid = Column("base_currency_oid", ForeignKey("Currencies.oid"))
    target_currency_oid = Column("target_currency_oid", ForeignKey("Currencies.oid"))
    rate = Column(DECIMAL, nullable=False)
