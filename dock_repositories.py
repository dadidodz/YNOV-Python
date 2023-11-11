from dock import SpaceDock
import pickle, os

class SpaceDockFileRepository:

    def __init__(self, name :str) -> None:
        self.name = name

    def save(self, dock: SpaceDock) -> None:
        self.picklefile = open(self.name, "wb")

        pickle.dump(dock, self.picklefile)

        self.picklefile.close()


    def load(self) -> SpaceDock:
        if not os.path.exists(self.name):
            spacedock = SpaceDockFileRepository(self.name)
            spacedock.save()
            return spacedock
        else:
            picklefile = open(self.name, "rb")

            output = pickle.load(picklefile)

            return output

        