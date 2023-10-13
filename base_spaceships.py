class Spaceship:
    """
    This is the documentation for Spaceship.

    Attribut : 
        is_alive(bool):Statut of the spaceship, dead of alive, default value is True.
    """
    is_alive = True

    def __init__(self, attack, defense):
        """
        This is the documentation for the __init__ method.
        Initialize the attributs attack and defense with the value of the parameters.

        Parameters:
        attack (int):The value of the attack of ship.
        defense (int):The value of the defense of ship.
        """
        self.attack = attack
        self.defense = defense

    def take_damages(self, damage):
        """
        This is the documentation for the takes_damage method.
        Subtract the damage passed in parameters to the ship defense.

        Parameters:
        damage (int):The value of the damage the ship takes.
        """
        if damage<0:
            raise ValueError("Negative damage")
        self.defense -= damage
        if self.defense<=0:
            self.defense=0
            self.is_alive = False