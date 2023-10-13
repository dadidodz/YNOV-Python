from spaceships import BattleshipKiller, Frigate, Interceptor, Bomber, Destroyer

if __name__ == '__main__':
    ship = BattleshipKiller()
    print(ship.attack)
    print(ship.defense)
    # fighter = Bomber()
    # print(fighter.defense)
    battleship = Frigate()
    print(battleship.defense)
    ship.fire_on(battleship)
    print(battleship.defense)