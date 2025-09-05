from enemy import Enemy
import random


class BOSS_BANDIT(Enemy):
    def attributes(self):
        self.health = 500
        self.attack_power = random.randint(0 ,500)

    def dash(self):
        dash_chance = random.randint(1, 3)
        if dash_chance == 1:
            input( "Press Enter to see the Boss Bandit dash!" )
            if input == "":
                print("The Boss Bandit dashes forward with incredible speed!")
                return self.attack_power * 3

