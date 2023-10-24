import random

from battle_simulator import Simulator
from spaceships import Interceptor, Frigate, Bomber, Destroyer

if __name__ == '__main__':
    random.seed(100)

    attackers = [Interceptor(), Interceptor(), Frigate()]
    defenders = [Bomber(), Interceptor(), Destroyer()]

    simulator = Simulator()

    simulator._simulate_fight(attackers, defenders)
    print(attackers[0].is_alive)
    print(attackers[1].is_alive)
    print(attackers[2].is_alive)
    print(defenders[0].is_alive)
    print(defenders[1].is_alive)
    print(defenders[2].is_alive)