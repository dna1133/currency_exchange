from fastapi import status

from currency_exchange.api.ischemas import ErrorSchema
from currency_exchange.api.schemas.currency_schemas import CurrencySchema

get_currencies_responce = {
    status.HTTP_200_OK: {"model": list[CurrencySchema]},
    status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
}

get_currency_responce = {
    status.HTTP_200_OK: {"model": CurrencySchema},
    status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
}

post_currency_responce = {
    status.HTTP_200_OK: {
        "description": "Currensy Added",
        "content": {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/CurrencySchema"},
            },
        },
    },
    status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
}
