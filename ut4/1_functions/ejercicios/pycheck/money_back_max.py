# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    money_back = {} 
    for currency in sorted(available_currencies, reverse=True):
        return_currency = to_give_back // currency
        amount = available_currencies[currency]
        if return_currency > amount:
            return_currency -= return_currency - amount
        to_give_back -= currency * return_currency
        money_back[currency] = return_currency
    money_back = {currency: amount for currency, amount in money_back.items() if amount > 0}
    if to_give_back > 0:
        money_back = None
    return money_back


if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})