from enum import Enum

from spaceships import Bomber, Cruiser, Destroyer, Frigate, Interceptor

class ShipType(Enum):
    CRUISER = Cruiser
    BOMBER = Bomber
    DESTROYER = Destroyer
    INTERCEPTOR = Interceptor
    FRIGATE = Frigate