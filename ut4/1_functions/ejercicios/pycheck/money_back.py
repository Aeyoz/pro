# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    money_back, debt = {}, 0
    to_give_back_copy = to_give_back
    available_currencies = sorted(available_currencies, reverse=True)
    for currency in available_currencies:
        return_currency = to_give_back_copy // currency
        to_give_back_copy %= currency
        if return_currency > 0:
            money_back[currency] = return_currency
        debt += currency * return_currency
    if debt < to_give_back:
        return None
    return money_back


if __name__ == '__main__':
    run(20, [5, 2, 1])