from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    _name: str
    _shop: str
    _price: float

    @property
    def name(self):
        return self._name

    @property
    def shop(self):
        return self._shop

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        raise TypeError("Можно складывать только объекты Product")


class Warehouse:
    def __init__(self):
        self._products: List[Product] = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")
        self._products.append(product)

    def print_product_by_index(self, index: int):
        if 0 <= index < len(self._products):
            print(self._products[index])
        else:
            print("Ошибка: неверный индекс")

    def print_product_by_name(self, name: str):
        found = False
        for product in self._products:
            if product.name == name:
                print(product)
                found = True
        if not found:
            print("Товар с таким именем не найден")

    def sort_by_name(self):
        self._products.sort(key=lambda p: p.name)

    def sort_by_shop(self):
        self._products.sort(key=lambda p: p.shop)

    def sort_by_price(self):
        self._products.sort(key=lambda p: p.price)


p1 = Product("Йогурт", "Евроопт", 80)
p2 = Product("Хлеб", "Копеечка", 50)
p3 = Product("Молоко", "Грошик", 57)

warehouse = Warehouse()
warehouse.add_product(p1)
warehouse.add_product(p2)
warehouse.add_product(p3)

print("По индексу 1")
warehouse.print_product_by_index(1)

print("\nПо имени 'Молоко'")
warehouse.print_product_by_name("Молоко")

print("\nСортировка по цене:")
warehouse.sort_by_price()
for product in warehouse._products:
    print(product)

print("\nСложение цен p1 + p3:")
print(p1 + p3)
