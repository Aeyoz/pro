# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    money_back, debt = {}, 0
    to_give_back_copy = to_give_back
    currencies = {currencie: amount for currencie, amount in sorted(available_currencies.items(), key=lambda x: x[0], reverse=True)}
    for currency in currencies:
        return_currency = to_give_back_copy // currency
        amount = currencies[currency]
        if return_currency > amount:
            return_currency -= return_currency - amount
        debt += currency * return_currency
        to_give_back_copy -= currency * return_currency
        if return_currency > 0:
            money_back[currency] = int(return_currency)
    if debt < to_give_back:
        return None
    return money_back




if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})