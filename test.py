from dock import SpaceDock
from dock_repositories import SpaceDockFileRepository
from spaceships import Interceptor, Frigate

if __name__ == '__main__':
    dock = SpaceDock()
    dock['default'] = [Interceptor(), Interceptor()]
    dock['defenders'] = [Frigate(), Frigate(), Interceptor()]
    print(dock)
    
    dock_repo = SpaceDockFileRepository('fleets.pickle')
    dock_repo.save(dock)
    
    retrieved_dock = dock_repo.load()
    print(retrieved_dock)