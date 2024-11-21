from fastapi import status

from currency_exchange.api.ischemas import ErrorSchema
from currency_exchange.api.schemas.exchange_schemas import (
    ExchangeRateChangedSchema,
    ExchangeSchema,
    ExchangePairAmountSchema,
)

get_all_exchange_rates_responce = {
    status.HTTP_200_OK: {"model": list[ExchangeSchema]},
    status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
}

get_exchange_rate_responce = {
    status.HTTP_200_OK: {"model": ExchangeSchema},
    status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
}

post_exchange_rate_responce = {
    status.HTTP_200_OK: {"model": ExchangeRateChangedSchema},
    status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
}

patch_exchange_rate_responce = {
    status.HTTP_200_OK: {"model": ExchangeRateChangedSchema},
    status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
}

get_exchange_sum_responce = {
    status.HTTP_200_OK: {"model": ExchangePairAmountSchema},
    status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
}
