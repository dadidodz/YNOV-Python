from dock import SpaceDock
from dock_repositories import SpaceDockInMemoryRepository, SpaceDockRepository, SpaceDockFileRepository

if __name__ == '__main__':
    dock = SpaceDock()
    dock_repo = SpaceDockInMemoryRepository()

    dock_repo.save(dock)
    print(dock_repo.load() == dock)