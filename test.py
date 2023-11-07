from dock import SpaceDock
from spaceships import Interceptor, Frigate

if __name__ == '__main__':
    dock = SpaceDock()
    

    default_fleet = dock['default'] #(dock.fleets['default'].ships)
    print(default_fleet.ships)
    # print(default_fleet.name)
    new_fleet = dock['this fleet does not exist yet']
    print(new_fleet.name, new_fleet.ships) #new_fleet.name = dock.fleets['this fleet does not exist yet'].name

    dock['my new fleet'] = [Interceptor(), Interceptor(), Frigate()]
    print(dock['my new fleet'].name, len(dock['my new fleet'].ships))

    
    
    # del dock['this fleet does not exist yet']
    # print(dock)