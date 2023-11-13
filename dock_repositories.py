from abc import ABC, abstractmethod
from dock import SpaceDock
import pickle, os

class SpaceDockRepository(ABC):
    
    @abstractmethod
    def save(self, dock: SpaceDock) -> None:
        pass

    @abstractmethod
    def load(self) -> SpaceDock:
        pass

class SpaceDockFileRepository(SpaceDockRepository):

    def __init__(self, name :str) -> None:
        self.name = name

    def save(self, dock: SpaceDock) -> None:
        self.picklefile = open(self.name, "wb")
        pickle.dump(dock, self.picklefile)
        self.picklefile.close()


    def load(self) -> SpaceDock:
        if not os.path.exists(self.name):
            spacedock = SpaceDock()
            return spacedock

        else:
            picklefile = open(self.name, "rb")
            output = pickle.load(picklefile)
            return output

class SpaceDockInMemoryRepository(SpaceDockRepository):
    
    space_dock : SpaceDock

    def save(self, dock: SpaceDock) -> None:
        self.space_dock = dock

    def load(self) -> SpaceDock:
        return self.space_dock
