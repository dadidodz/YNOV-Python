# from fastapi import FastAPI
import os
from dock_repositories import SpaceDockInMemoryRepository, SpaceDockFileRepository

# app = FastAPI()


def init_dock_repository():
    value = os.environ['DOCK_REPOSITORY'].lower()
    match value:
        case 'in_memory' :
            return SpaceDockInMemoryRepository()
        case 'file':
            return SpaceDockFileRepository(value)
        case _:
            raise ValueError('Repository ' + value + ' does not exist')