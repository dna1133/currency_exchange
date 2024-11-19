from pydantic import BaseModel


class CurrencySchema(BaseModel):
    fullname: str
    code: str
    sign: str
    oid: str
