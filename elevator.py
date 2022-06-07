import random


class Building:
    level = None

    def __init__(self):
        self.level = list(range(1, random.randrange(5, 21)))


class Elevator:
    def __init__(self):
        self.max_passenger = 5
        self.elevator_load = []
        self.current_level = 1
        self.last_level = len(building.level)

    def move_up(self):
        for lev in building.level:
            if lev in self.elevator_load:
                self.out_lift(lev)
                print(f'люди вышли из {lev} этажа')
                continue
            for i in passenger.amount_passenger[lev]:
                if len(self.elevator_load) < self.max_passenger:
                    if i > lev:
                        self.elevator_load.append(i)
                        del passenger.amount_passenger[lev][0]
                        print(f'Этаж {lev}, люди зашли в 'f'{self.elevator_load}')
                        continue
                elif len(self.elevator_load) == self.max_passenger:
                    continue

    def move_down(self):
        pass

    def in_lift(self, value):
        self.elevator_load.append(value)

    def out_lift(self, value):
        self.elevator_load.remove(value)


class Passenger:
    def __init__(self):
        self.amount_passenger = {}
        for i in building.level:
            rand_level = list(range(1, i)) + list(range(i + 1, len(building.level)))
            self.amount_passenger[i] = [random.choice(rand_level) for x in range(random.randrange(1, 11))]


if __name__ == "__main__":
    building = Building()
    passenger = Passenger()
    print('***step 1 ***')
    lift = Elevator()
    lift.move_up()
    
    