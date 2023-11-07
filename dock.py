from fleet import Fleet

class SpaceDock:
    
    def __init__(self) -> None:
        # the fleets instance attribute store all user fleets in a dict by name.
        self.fleets = {'default': Fleet('default', [])}

    def __getitem__(self, key):
        if key in self.fleets:
            return self.fleets[key]
        else:
            self[key]=''
            return self.fleets[key]
    
    def __setitem__(self, key, newvalue):
        # self.fleets[key] = key
        self.fleets = {key : Fleet(key, [])}