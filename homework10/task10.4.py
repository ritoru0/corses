import math

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        cx, cy, cz = self.center 
        distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2)
        return distance <= self.radius


s2 = Sphere(3, 1, 2, 3)
print("Объем сферы:", s2.get_volume())
print("Площадь поверхности:", s2.get_square())
print("Радиус:", s2.get_radius())
print("Центр:", s2.get_center())
print("Точка внутри?", s2.is_point_inside(2, 2, 3))

s2.set_radius(5)
s2.set_center(0, 0, 0)
print("Новый радиус:", s2.get_radius())
print("Новый центр:", s2.get_center())
