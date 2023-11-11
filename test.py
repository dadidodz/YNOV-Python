from space_yard import SpaceYard
from spaceships import Interceptor
from dock import SpaceDock

if __name__ == '__main__':
    dock = SpaceDock()
    # yard = SpaceYard(dock)
    
    # yard.build_ship('default', Interceptor, 3, 4000, 600)
    print(dock)
    
    # yard.build_ship('default', Interceptor, 3, 2000, 600)