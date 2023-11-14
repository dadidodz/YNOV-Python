import os
from app import init_dock_repository

if __name__ == '__main__':
    os.environ['DOCK_REPOSITORY'] = 'in_memory'
    print(type(init_dock_repository()))

    os.environ['DOCK_REPOSITORY'] = 'inCORrect'
    init_dock_repository()