from enemy import Enemy


class Goblin(Enemy):
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name, color="green"):
        super().__init__(name)
        self.color = color
        self.health = 50