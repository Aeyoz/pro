from __future__ import annotations
from pathlib import Path

class Product:
    def __init__(self, product_code, stock, price=0):
        self.code = product_code
        self.stock = stock
        self.price = price

class Vending:
    def __init__(self):
        self.cash = 0
        pass

    def change_stock(self, other, stock):
        other.stock = stock
        pass

    def change_price(self, other, price):
        pass

    def __setitem__(self, item, value):
        pass

    def __getitem__(self):
        pass

class Transaction:
    def __init__(self, operations):
        pass

    def order(self, amount: int, cash: int, vending: dict) -> dict:
        debt = amount * vending["products"][product][1]
        if cash >= debt and amount <= vending["products"][product][0]:
            vending["products"][product][0] -= amount
            vending["cash"] += debt
        return vending





def read_operations(operations_path: Path):
    processed_operations = []
    with open(operations_path) as operations:
        entry_operations = "".join(operations).strip().split("\n")
        for i, operation in enumerate(entry_operations, start=0):
            processed_operations.append([])
            subelements = operation.split()
            for subelement in subelements:
                if subelement.isdigit():
                    processed_operations[i].append(int(subelement))
                else:
                    processed_operations[i].append(subelement)
    return processed_operations

def write_status(status_path: Path, vending: dict):
    with open(status_path, "w") as output: 
        output.write(f'{vending["cash"]}\n')
        for product, p_info in sorted(vending["products"].items()):
            stock, price = p_info
            output.write(f"{product} {stock} {price}\n")