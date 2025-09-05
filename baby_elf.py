from enemy import Enemy


# A new special ability
class baby_elf(Enemy):
    def cry():
        print("Waaah Waaah")

    # Override the take_damage method to prevent damage
    def take_damage(self, damage):
        print("Why are you attack a baby? YOU MONSTER!")
        return
