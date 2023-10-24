from base_spaceships import Spaceship

class Simulator:
    @staticmethod
    def _duel_fight(attack_spaceship : Spaceship, defense_spaceship : Spaceship) -> None:
        attack_spaceship.fire_on(defense_spaceship)
        if defense_spaceship.is_alive == True:
            defense_spaceship.fire_on(attack_spaceship)
