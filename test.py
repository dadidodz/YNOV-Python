from base_spaceships import Spaceship

if __name__ == '__main__':
    uss_enterprise = Spaceship(attack=100, defense=1500)
    uss_enterprise.take_damages(2000)
    print(uss_enterprise.defense)
    print(uss_enterprise.is_alive)