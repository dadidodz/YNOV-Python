from fleet import Fleet
from spaceships import Interceptor, Frigate

if __name__ == '__main__':
    fighter_1 = Interceptor()
    fighter_2 = Interceptor()
    fighter_3 = Interceptor()
    tentive_iv = Frigate()

    alpha_fleet = Fleet('alpha group', [fighter_1])
    print(len(alpha_fleet.ships))

    alpha_fleet + fighter_2
    print(len(alpha_fleet.ships))

    alpha_fleet + [fighter_3, tentive_iv]
    print(len(alpha_fleet.ships))