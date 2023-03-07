# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    money_back = {} 
    for currency in sorted(available_currencies, reverse=True):
        if to_give_back > 0:
            return_currency = to_give_back // currency
            amount = available_currencies[currency]
            _min = min(amount, return_currency)
            to_give_back -= currency * _min
            money_back[currency] = _min
    if to_give_back > 0:
        money_back = None
    return money_back




if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})