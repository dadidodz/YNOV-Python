from enum import Enum

from spaceships import Bomber, Cruiser, Destroyer, Frigate, Interceptor

class ShipType(Enum):
    CRUISER = Cruiser
    BOMBER = Bomber
    DESTROYER = Destroyer
    INTERCEPTOR = Interceptor
    FRIGATE = Frigate

def get_ship_class_by_name(ship_name:str):
    ship_name = ship_name.upper()
    # ship_name = ship_name.lower()
    # ship_name = ship_name.capitalize()
    if ship_name == ShipType.CRUISER.name:
        return ShipType.CRUISER
    elif ship_name == ShipType.BOMBER.name:
        return ShipType.BOMBER
    elif ship_name == ShipType.DESTROYER.name:
        return ShipType.DESTROYER
    elif ship_name == ShipType.INTERCEPTOR.name:
        return ShipType.INTERCEPTOR
    elif ship_name == ShipType.FRIGATE.name:
        return ShipType.FRIGATE
    else:
        raise ValueError()
    
    