import random
import time
from goblin import Goblin
from hero import Hero
from boss import BOSS_BANDIT

# custom print with delay
def slow_print(*args, **kwargs):
    print(*args, **kwargs)
    time.sleep(0.1)  # every line waits 0.1s

def main():
    slow_print("Welcome to the Battle Arena!")
    slow_print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    hero = Hero("Maxwell")
    goblins = [Goblin(f"Goblin {i+1}") for i in range(5)]
    defeated_goblins = 0
    total_damage_dealt = 0
    round_of_game = 0

    while hero.is_alive() and any(g.is_alive() for g in goblins):
        slow_print("\nNew Round!")

        # Hero's turn
        target_goblin = random.choice([g for g in goblins if g.is_alive()])
        damage = hero.strike()
        slow_print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        total_damage_dealt += damage
        target_goblin.take_damage(damage)

        if not target_goblin.is_alive():
            defeated_goblins += 1
            slow_print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                slow_print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

        round_of_game += 1
        slow_print("BOSS BANDIT HAS ENTERED THE ARENA!")

        boss_bandit = BOSS_BANDIT("Boss Bandit")
        while boss_bandit.is_alive() and hero.is_alive():
            damage = hero.strike()
            slow_print(f"Hero attacks {boss_bandit.name} for {damage} damage!")
            total_damage_dealt += damage
            boss_bandit.take_damage(damage)

            if not boss_bandit.is_alive():
                slow_print(f"{boss_bandit.name} has been defeated!")
                break

            damage = boss_bandit.attack()
            slow_print(f"{boss_bandit.name} attacks hero for {damage} damage!")
            hero.receive_damage(damage)

            dash_damage = boss_bandit.dash()
            if dash_damage:
                slow_print(f"{boss_bandit.name} dashes and deals {dash_damage} damage!")
                hero.receive_damage(dash_damage)

        slow_print(f"End of Round {round_of_game}. Hero's health: {hero.health}")

    slow_print(f"There were {round_of_game} rounds in this game.")

    if hero.is_alive():
        if boss_bandit.is_alive() == False:
            print("THE BOSS BANDIT HAS BEEN DEFEATED!")
        else:
            print("THE BOSS BANDIT IS STILL ALIVE!")
        slow_print("\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        slow_print("\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    slow_print(f"\nBattle Summary:" +
               f"\nTotal damage dealt by hero: {total_damage_dealt}" +
               f"\nRounds Survived: {round_of_game}")

    slow_print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")


if __name__ == "__main__":
    main()