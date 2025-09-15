from dataclasses import dataclass, field

@dataclass
class Bus:
    speed: int
    max_seats: int
    max_speed: int
    passengers: list = field(default_factory=list)
    seats: dict = field(default_factory=dict)

    @property
    def has_free_seats(self):
        return len(self.passengers) < self.max_seats

    def board(self, *names):
        for name in names:
            if not self.has_free_seats:
                raise ValueError("Свободных мест нет!")
            if name in self.passengers:
                raise ValueError(f"Пассажир {name} уже в автобусе")
            self.passengers.append(name)
            for seat_num in range(1, self.max_seats + 1):
                if seat_num not in self.seats:
                    self.seats[seat_num] = name
                    break

    def leave(self, *names):
        for name in names:
            if name not in self.passengers:
                raise ValueError(f"Пассажир {name} не найден в автобусе")
            self.passengers.remove(name)
            seats_to_remove = [seat for seat, occupant in self.seats.items() if occupant == name]
            for seat in seats_to_remove:
                del self.seats[seat]

    def increase_speed(self, delta):
        new_speed = self.speed + delta
        if new_speed > self.max_speed:
            raise ValueError("Скорость превышает максимальную")
        self.speed = new_speed

    def decrease_speed(self, delta):
        new_speed = self.speed - delta
        if new_speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self.speed = new_speed

    def __contains__(self, name):
        return name in self.passengers

    def __iadd__(self, name):
        self.board(name)
        return self

    def __isub__(self, name):
        self.leave(name)
        return self



bus = Bus(speed=50, max_seats=3, max_speed=100)

bus.board("Иванов", "Петров")
print( bus.passengers)

bus.increase_speed(40)
print( bus.speed)
