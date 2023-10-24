from typing import override
from base_spaceships import Battleship, Fighter

class Fleet:

    def __init__(self, name:str, ships:list):
        self.name = name
        self.ships = ships

    @override
    def __add__(self, other):
        if isinstance(other, list):
            for element in other:
                self.ships.append(element)
        else:
            self.ships.append(other)
            
    def get_all_alive_ships(self):
        return [ship for ship in self.ships if ship.is_alive]
    
    def get_alive_battleships(self):
        return [ship for ship in self.ships if ship.is_alive and isinstance(ship, Battleship)]

    def get_alive_fighters(self):
        return [ship for ship in self.ships if ship.is_alive and isinstance(ship, Fighter)]
    
    def get_report(self):
        alive_battleships = len(self.get_alive_battleships())
        alive_fighters = len(self.get_alive_fighters())
        dead_battleships = len([ship for ship in self.ships if not ship.is_alive and isinstance(ship, Battleship)])
        dead_fighters = len([ship for ship in self.ships if not ship.is_alive and isinstance(ship, Fighter)])

        return {
            'alive_battleships': alive_battleships,
            'alive_fighters': alive_fighters,
            'dead_battleships': dead_battleships,
            'dead_fighters': dead_fighters,
        }
    
    @property
    def alive_ships(self):
        return self.get_all_alive_ships()

    @property
    def alive_fighters(self):
        return self.get_alive_fighters()

    @property
    def alive_battleships(self):
        return self.get_alive_battleships()

    @property
    def report(self):
        return self.get_report()