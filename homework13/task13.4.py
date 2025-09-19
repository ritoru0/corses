from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав!!!"

class Cat(Animal):
    def speak(self):
        return "Мяу!!!"

class AnimalFactory:
    def create_animal(self, animal_type: str):
        animal_type = animal_type.lower()
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Неизвестный вид животного: {animal_type}")

factory = AnimalFactory()

dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())  
print(cat.speak())  
