from dock import SpaceDock
from spaceships import Interceptor, Frigate

if __name__ == '__main__':
    dock = SpaceDock()

    default_fleet = dock['default']
    print(default_fleet.ships)

    new_fleet = dock['this fleet does not exist yet']
    print(new_fleet.name, new_fleet.ships)

    dock['my new fleet'] = [Interceptor(), Interceptor(), Frigate()]
    print(dock['my new fleet'].name, len(dock['my new fleet'].ships))

    print(dock)
    
    del dock['this fleet does not exist yet']
    print(dock)