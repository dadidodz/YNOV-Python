from base_spaceships import Spaceship
from requirements import Requirements
from spaceships import Interceptor, Frigate, Bomber, Destroyer, Cruiser

if __name__ == '__main__':
    print(Interceptor.requirements.metal)
    print(Bomber.requirements.crystal)
    print(Cruiser.requirements.metal)

    