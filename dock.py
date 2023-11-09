from fleet import Fleet

class SpaceDock:
    
    def __init__(self) -> None:
        # the fleets instance attribute store all user fleets in a dict by name.
        self.fleets = {'default': Fleet('default', [])}

    def __getitem__(self, key):
        if key in self.fleets.keys():
            return self.fleets[key]
        else:
            self[key]=None
            return self.fleets[key]
    
    def __setitem__(self, key, newvalue):
        if newvalue == None:
            self.fleets[key] = Fleet(key, [])
        elif not key in self.fleets.keys():
            self.fleets[key] = Fleet(key, [])
            self.fleets[key]+(newvalue)

    def __delitem__(self, key):
        if key in self.fleets.keys():
            self.fleets.pop(key)

    def __str__(self):
        string = ''
        for fleet in self.fleets:
            string += str(self.fleets[fleet].name) + ': ' + str(len(self.fleets[fleet].ships)) + ' ships, '

        string = string.strip()
        string = string[:-1]
        return string
        