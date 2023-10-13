

from base_spaceships import Battleship, Fighter


class Interceptor(Fighter):
    def __init__(self, attack=180, defense=1000):
        super().__init__(attack, defense)

    def fire_on(self, spaceship):
        if isinstance(spaceship, Fighter):
            spaceship.take_damages(self.attack*2)
        else:
            spaceship.take_damages(self.attack)

class Bomber(Fighter):
    def __init__(self, attack=150, defense=2000):
        super().__init__(attack, defense)

    def fire_on(self, spaceship):
        if isinstance(spaceship, Battleship):
            spaceship.take_damages(self.attack*2)
        else:
            spaceship.take_damages(self.attack)

class Cruiser (Battleship):
    def __init__(self, attack=800, defense=3000):
        super().__init__(attack, defense)

class Frigate (Battleship):
    def __init__(self, attack=500, defense=2500):
        super().__init__(attack, defense)

    def fire_on(self, spaceship):
        if isinstance(spaceship, Fighter):
            spaceship.take_damages(self.attack*2)
        else:
            spaceship.take_damages(self.attack)

class Destroyer (Battleship):
    def __init__(self, attack=650, defense=5000):
        super().__init__(attack, defense)

    def fire_on(self, spaceship):
        if isinstance(spaceship, Battleship):
            spaceship.take_damages(self.attack*2)
        else:
            spaceship.take_damages(self.attack)