class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self): #магический метод 
        if self.flavor:
            return f"У вас газировка с {self.flavor} вкусом"
        else:
            return "У вас обычная газировка"



s1 = Soda("клубничным")
print(s1)  

s2 = Soda()
print(s2) 
