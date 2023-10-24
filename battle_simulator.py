import random
from base_spaceships import Spaceship

class Simulator:
    @staticmethod
    def _duel_fight(attack_spaceship : Spaceship, defense_spaceship : Spaceship) -> None:
        attack_spaceship.fire_on(defense_spaceship)
        if defense_spaceship.is_alive == True:
            defense_spaceship.fire_on(attack_spaceship)

    def _simulate_fight(self, attacker_ships_list:list, defenser_ships_list:list):
        if not len(attacker_ships_list) or not len(defenser_ships_list):
            pass
        else:
            for ship in attacker_ships_list:
                if ship.is_alive:
                    ship.fire_on(defenser_ships_list[random.randint(0, len(defenser_ships_list)-1)])