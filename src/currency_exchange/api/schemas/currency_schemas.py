from pydantic import BaseModel


class CurrencySchema(BaseModel):
    fullname: str
    code: str
    sign: str
    oid: str

    class Config:
        from_attributes = True
