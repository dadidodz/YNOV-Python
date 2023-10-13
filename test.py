from spaceships import Interceptor, Bomber, Destroyer

if __name__ == '__main__':
    tie_interceptor = Interceptor()
    y_wing = Destroyer()
    print(y_wing.attack)
    print(y_wing.defense)

    print(tie_interceptor.defense)
    y_wing.fire_on(tie_interceptor)
    print(tie_interceptor.defense)
