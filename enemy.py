import random

class Enemy:
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = random.randint(5, 15)

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        if damage > self.health:
            self.health = 0
        print(f"{self.name} takes {damage} damage. health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
