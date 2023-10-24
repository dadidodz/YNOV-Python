from battle_simulator import Simulator
from spaceships import Interceptor, Frigate, Bomber

if __name__ == '__main__':
    tie_fighter = Interceptor()
    y_wing = Bomber()

    simulator = Simulator()

    simulator._duel_fight(tie_fighter, y_wing)
    print(tie_fighter.defense)
    print(y_wing.defense)

    tentative_iv = Frigate()
    tie_fighter = Interceptor()

    simulator._duel_fight(tentative_iv, tie_fighter)
    print(tentative_iv.defense)
    print(tie_fighter.is_alive)