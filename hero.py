import random


class Hero:
    """
    This is our hero blueprint.

    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """

    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.attack_power = random.randint(0, 100)

    def strike(self):
        hero_damage = 0
        chance = random.randint(1, 2)
        if chance == 1:
            print("Critical Strike!")
            return self.attack_power * 2
        else:
            return self.attack_power
    
    
    def receive_damage(self, damage):
        self.health -= damage
        if damage > self.health:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
