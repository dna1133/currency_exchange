from sqlalchemy import Column, String
from currency_exchange.gateways.database.models.base import Base


class Currencies(Base):
    __tablename__ = "Currencies"

    oid = Column(String, primary_key=True, unique=True)
    code = Column(String, nullable=False, unique=True)
    fullname = Column(String, nullable=False)
    sign = Column(String, nullable=False)
