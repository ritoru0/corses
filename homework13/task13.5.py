from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(Strategy):
    def execute(self, a, b):
        return a + b

class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b

class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b

class Division(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль!")
        return a / b

class Calculator:
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        if not self._strategy:
            raise ValueError("Стратегия не установлена")
        return self._strategy.execute(a, b)


calc = Calculator()

calc.set_strategy(Addition())
print(calc.calculate(18, 6))  

calc.set_strategy(Subtraction())
print(calc.calculate(15, 5))  

