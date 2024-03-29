from requirements import Requirements
class Spaceship:
    """
    Spaceship class

    Attribut : 
        is_alive(bool):Statut of the spaceship, dead of alive, default value is True.
    """
    is_alive = True
    requirements : Requirements

    def __init__(self, requirements, attack=100, defense=100):
        """
        Initialize the attributs attack and defense with the value of the parameters.

        Parameters:
        attack (int):The value of the attack of ship.
        defense (int):The value of the defense of ship.
        """
        self.requirements = requirements
        self.attack = attack
        self.defense = defense
        
    def take_damages(self, damage):
        """
        Subtract the damage passed in parameters to the ship defense.

        Parameters:
        damage (int):The value of the damage the ship takes. Can't be negative.
        """
        if damage<0:
            raise ValueError("Negative damage")
        self.defense -= damage
        if self.defense<=0:
            self.defense=0
            self.is_alive = False
    
    def fire_on(self, spaceship):
        """
        Deals damages to the spaceship passed in parameters.

        Parameters:
        spaceship (Spaceship):Targetted spaceship.
        """
        spaceship.take_damages(self.attack)

class Battleship(Spaceship):
    """
    A class representing a battleship, inheriting from Spaceship.
    """
    def __init__(self, attack, defense):
        super().__init__(attack, defense)
        
class Fighter(Spaceship):
    """
    A class representing a fighter, inheriting from Spaceship.
    """
    def __init__(self, attack, defense):
        super().__init__(attack, defense)