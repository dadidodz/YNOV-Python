import os
from dock_repositories import SpaceDockInMemoryRepository, SpaceDockFileRepository

def init_dock_repository():
    value = os.environ['DOCK_REPOSITORY'].lower()
    # print(type(value))
    # if value=='in_memory' :
    #     print('1')
    # elif value =='file':
    #     print('2')
    # else:
    #     raise ValueError('Repository ' + value + ' does not exist')
    match value:
        case 'in_memory' :
            return SpaceDockInMemoryRepository()
        case 'file':
            return SpaceDockFileRepository()
        case _:
            raise ValueError('Repository ' + value + ' does not exist')