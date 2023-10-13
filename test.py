from base_spaceships import Battleship, Fighter

if __name__ == '__main__':
    x_wing = Fighter(attack=200, defense=800)
    print(x_wing.attack)
    print(x_wing.defense)