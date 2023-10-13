from base_spaceships import Spaceship

if __name__ == '__main__':
    uscss_nostromo = Spaceship(attack=100, defense=1500)
    print(uscss_nostromo.is_alive)
    print(uscss_nostromo.attack)
    print(uscss_nostromo.defense)