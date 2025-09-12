class Car:
    def __init__ (self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
        
    def turn_on(self):
        print("Автомобиль заведён")
    
    def turn_off(self):
        print("Автомобиль заглушён")
    
    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color
        
car = Car("красный", "седан", 2020)
car.turn_on()
car.set_color("синий")  
print(car.color)        

class Car2:
    def __init__(self, color, type, year):
        self._color = color
        self._type = type
        self._year = year

    def turn_on(self):
        print("Автомобиль заведён")

    def turn_off(self):
        print("Автомобиль заглушён")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value


car = Car("красный", "седан", 2020)
car.turn_on()
print(car.color)   
car.color = "синий"
print(car.color)   
car.year = 2022
print(car.year)    
car.turn_off()
