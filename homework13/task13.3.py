from dataclasses import dataclass

@dataclass
class Pizza:
    size: str
    cheese: bool = False
    pepperoni: bool = False
    mushrooms: bool = False
    onions: bool = False
    bacon: bool = False


class PizzaBuilder:
    def __init__(self, size):
        self.pizza = Pizza(size)

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        return (self.builder
                .add_cheese()
                .add_pepperoni()
                .add_mushrooms()
                .add_onions()
                .add_bacon()
                .build())


builder = PizzaBuilder("Большая")
director = PizzaDirector(builder)
pizza = director.make_pizza()
print(pizza)
