from dataclasses import dataclass

@dataclass
class BeeElephant:
    bee: int
    elephant: int

    def Fly(self):
        return self.bee >= self.elephant

    def Trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def Eat(self, meal, value):
        if meal not in ("nectar", "grass"):
            raise ValueError("Питание должно быть 'nectar' или 'grass'")

        if meal == "nectar":
            self.bee = min(self.bee + value, 100)
            self.elephant = max(self.elephant - value, 0)
        else:
            self.elephant = min(self.elephant + value, 100)
            self.bee = max(self.bee - value, 0)

be = BeeElephant(40, 60)

print("Fly:", be.Fly())  

print("Trumpet:", be.Trumpet())  

be.Eat("nectar", 30)
print("После еды нектара:", be)

be.Eat("grass", 50)
print("После еды травы:", be)


