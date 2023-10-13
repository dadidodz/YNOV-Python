from base_spaceships import Battleship, Fighter, Spaceship

class FighterKiller(Spaceship):
    def __init__(self, attack=800, defense=2800):
        super().__init__(attack, defense)

    def fire_on(self, spaceship):
        if isinstance(spaceship, Fighter):
            spaceship.take_damages(self.attack*2)
        else:
            spaceship.take_damages(self.attack)

class BattleshipKiller(Spaceship):
    def __init__(self, attack=800, defense=900):
        super().__init__(attack, defense)
    
    def fire_on(self, spaceship):
        if isinstance(spaceship, Battleship): 
            spaceship.take_damages(self.attack*2)
        else:
            spaceship.take_damages(self.attack)

class Cruiser (Battleship):
    def __init__(self, attack=800, defense=3000):
        super().__init__(attack, defense)

class Bomber(Fighter, BattleshipKiller):
    def __init__(self, attack=150, defense=2000):
        super().__init__(attack, defense)

class Destroyer (Battleship, BattleshipKiller):
    def __init__(self, attack=650, defense=5000):
        super().__init__(attack, defense)

class Interceptor(Fighter, FighterKiller):
    def __init__(self, attack=180, defense=1000):
        super().__init__(attack, defense)

class Frigate (Battleship, FighterKiller):
    def __init__(self, attack=500, defense=2500):
        super().__init__(attack, defense)

