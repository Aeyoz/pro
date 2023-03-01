# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    money_back = {}
    for currency in sorted(available_currencies, reverse=True):
        if not to_give_back:
            return money_back
        return_currency = to_give_back // currency
        to_give_back %= currency
        money_back[currency] = money_back.get(currency, 0) + return_currency
    if to_give_back > 0:
        return None
    return money_back


if __name__ == '__main__':
    run(20, [5, 2, 1])