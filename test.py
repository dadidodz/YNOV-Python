from base_spaceships import Spaceship

if __name__ == '__main__':
    tie_fighter = Spaceship(50, 300)
    millennium_falcon = Spaceship(350, 900)
    
    tie_fighter.fire_on(millennium_falcon)
    print(millennium_falcon.defense)
    print(millennium_falcon.is_alive)
    
    millennium_falcon.fire_on(tie_fighter)
    print(tie_fighter.defense)
    print(tie_fighter.is_alive)