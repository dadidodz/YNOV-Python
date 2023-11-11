from dock import SpaceDock
from spaceships import Spaceship, Interceptor

class SpaceYard:

    def __init__(self, spacedock:SpaceDock) -> None:
        self.spacedock = spacedock

    def build_ship(self, fleet_name:str, ship_class:Spaceship, quantity:int, available_metal:int, available_crystal:int):
        a = ship_class.requirements.metal
        b = ship_class.requirements.crystal
        if a < available_metal and b < available_crystal:
            self.spacedock.fleets[fleet_name] = [Interceptor(), Interceptor(),Interceptor()]
        
        if self.__class__.__base__.__name__ == fleet_name or self.__class__.__name__ == fleet_name:
            pass