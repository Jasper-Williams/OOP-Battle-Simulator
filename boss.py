from enemy import Enemy
import random


class BOSS_BANDIT(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500
        self.attack_power = random.randint(1, 500)

    def attack(self):
        return random.randint(1, self.attack_power)

    def dash(self):
        dash_chance = random.randint(1, 2)
        if dash_chance == 1:
            input("Press Enter to see the Boss Bandit dash!")
            if input == "":
                print("The Boss Bandit dashes forward with incredible speed!")
                return self.attack_power * 3

