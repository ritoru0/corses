class Math:
    def __init__(self):
        pass

    def addition(self, a, b):
        print(a + b)

    def subtraction(self, a, b):
        print(a - b)

    def multiplication(self, a, b):
        print(a * b)

    def division(self, a, b):
        if b == 0:
            raise ValueError("Ошибка: деление на ноль")
        print(a / b)


m = Math()
m.addition(5, 3)        
m.subtraction(5, 3)     
m.multiplication(5, 3)  
m.division(5, 2)        

class Math2:
    @staticmethod
    def addition(a, b):
        print(a + b)

    @staticmethod
    def subtraction(a, b):
        print(a - b)

    @staticmethod
    def multiplication(a, b):
        print(a * b)

    @staticmethod
    def division(a, b):
        if b == 0:
            raise ValueError("Ошибка: деление на ноль")
        print(a / b)

Math2.addition(5, 3)        
Math2.subtraction(5, 3)     
Math2.multiplication(5, 3)  
Math2.division(5, 2)        
