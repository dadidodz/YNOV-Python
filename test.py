import random
from battle_simulator import Simulator
from spaceships import Interceptor, Frigate, Bomber, Destroyer
from fleet import Fleet

if __name__ == '__main__':
    random.seed(100)

    attackers = Fleet('Empire', [Interceptor(), Interceptor(), Frigate()])
    defenders = Fleet('Rebels', [Bomber(), Interceptor(), Destroyer()])

    simulator = Simulator(attackers, defenders)

    simulator.fight()
    print(attackers.ships[0].is_alive)
    print(attackers.ships[1].is_alive)
    print(attackers.ships[2].is_alive)
    print(defenders.ships[0].is_alive)
    print(defenders.ships[1].is_alive)
    print(defenders.ships[2].is_alive)
    print(simulator.get_report())