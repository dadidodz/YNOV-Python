from spaceships import Interceptor, Bomber, Destroyer

if __name__ == '__main__':
    tie_interceptor = Interceptor()
    y_wing = Bomber()

    print(tie_interceptor.attack)
    print(y_wing.defense)

    tie_interceptor.fire_on(y_wing)
    print(y_wing.defense)

    venator = Destroyer()
    print(venator.defense)
    tie_interceptor.fire_on(venator)
    print(venator.defense)