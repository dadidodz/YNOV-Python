from spaceships import Interceptor, Bomber, Destroyer

if __name__ == '__main__':
    tie_interceptor1 = Interceptor()
    tie_interceptor2 = Interceptor()
    print(tie_interceptor1.attack)
    print(tie_interceptor2.defense)
    tie_interceptor1.fire_on(tie_interceptor2)
    print(tie_interceptor2.defense)