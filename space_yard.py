from dock import SpaceDock
from spaceships import Spaceship
from exceptions import ResourceError

class SpaceYard:

    def __init__(self, spacedock:SpaceDock) -> None:
        self.spacedock = spacedock

    def build_ship(self, fleet_name:str, ship_class:Spaceship, quantity:int, available_metal:int, available_crystal:int):
        if ship_class.requirements.metal*quantity <= available_metal and ship_class.requirements.crystal*quantity <= available_crystal:
            for i in range(quantity):
                self.spacedock[fleet_name]+(ship_class())
        else:
            string = 'Not enough '
            if ship_class.requirements.metal*quantity > available_metal:
                string += 'metal'
            else:
                string += 'crystal'
            string += ' to build ' + str(quantity) + ' ' + type(ship_class()).__name__
            if quantity > 1:
                string+= 's'
            raise ResourceError(string)