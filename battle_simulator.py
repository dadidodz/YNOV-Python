import random
from base_spaceships import Spaceship
from fleet import Fleet

class Simulator:

    def __init__ (self, attacker_fleet :Fleet, defender_fleet: Fleet) -> None:
        self.attacket_fleet = attacker_fleet
        self.defender_fleet = defender_fleet

    @staticmethod
    def _duel_fight(attack_spaceship : Spaceship, defense_spaceship : Spaceship) -> None:
        attack_spaceship.fire_on(defense_spaceship)
        if defense_spaceship.is_alive:
            defense_spaceship.fire_on(attack_spaceship)

    def _simulate_fight(self, attacker_ships_list:list, defenser_ships_list:list):
        if not len(attacker_ships_list) or not len(defenser_ships_list):
            pass
        else:
            for ship in attacker_ships_list:
                if ship.is_alive:
                    self._duel_fight(ship, defenser_ships_list[random.randint(0, len(defenser_ships_list)-1)])

    def fight(self):
        self._simulate_fight(self.attacket_fleet.alive_battleships, self.defender_fleet.alive_battleships)
        self._simulate_fight(self.attacket_fleet.alive_fighters, self.defender_fleet.alive_fighters)
        self._simulate_fight(self.attacket_fleet.alive_ships, self.defender_fleet.alive_ships)

    def get_report(self):
        return {
            self.attacket_fleet.name: self.attacket_fleet.report,
            self.defender_fleet.name: self.defender_fleet.report,
        }