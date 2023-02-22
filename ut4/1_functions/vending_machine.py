stock = {"ambrosia": {"stock": 1, "price":0.8},
        "cocacola": {"stock": 10, "price":1.2},
        "gum": {"stock": 5, "price":0.2},
        "lollipop": {"stock": 13, "price":0.5},
        "huevo kinder": {"stock": 40, "price":1.8}}


def vending_machine(money=0, **articles):
    debt = 0
    for article, cuantity in articles.items():
        debt += stock.get(article).get("price") * cuantity
    return money - debt
print(stock)
print(vending_machine(money=30, cocacola=2, ambrosia=1, gum=1))