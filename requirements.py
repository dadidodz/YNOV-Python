from dataclasses import dataclass

@dataclass
class Requirements:
    metal : int
    crystal : int

    def __init__(self, metal: int, crystal: int):
        self.metal = metal
        self.crystal = crystal