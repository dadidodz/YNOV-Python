from fleet import Fleet
from spaceships import Frigate, Cruiser, Interceptor

if __name__ == '__main__':
    uss_kelvin = Frigate()
    star_fleet = Fleet('Starfleet', [uss_kelvin, Cruiser(), Interceptor(), Cruiser()])
    print(star_fleet.name)
    print(len(star_fleet.ships))

    uss_kelvin.is_alive = False
    print(len(star_fleet.get_alive_battleships()))
    print(star_fleet.get_report())

    print(star_fleet.report == star_fleet.get_report())
    print(star_fleet.alive_fighters == star_fleet.get_alive_fighters())