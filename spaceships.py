

from base_spaceships import Battleship, Fighter

class Cruiser (Battleship):
    def __init__(self, attack=800, defense=3000):
        super().__init__(attack, defense)


class BattleshipKiller():
    def fire_on(self, spaceship):
        if isinstance(spaceship, Battleship): 
            spaceship.take_damages(self.attack*2)
        else:
            spaceship.take_damages(self.attack*2)

class Bomber(BattleshipKiller, Fighter):
    def __init__(self, attack=150, defense=2000):
        super().__init__(attack, defense)

class Destroyer (BattleshipKiller, Battleship):
    def __init__(self, attack=650, defense=5000):
        super().__init__(attack, defense)


class FighterKiller():
    def fire_on(self, spaceship):
        if isinstance(spaceship, Fighter):
            spaceship.take_damages(self.attack*2)
        else:
            spaceship.take_damages(self.attack*2)

class Interceptor(FighterKiller, Fighter):
    def __init__(self, attack=180, defense=1000):
        super().__init__(attack, defense)

class Frigate (FighterKiller, Battleship):
    def __init__(self, attack=500, defense=2500):
        super().__init__(attack, defense)