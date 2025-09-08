import random
from goblin import Goblin
from hero import Hero
from boss import BOSS_BANDIT


def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    hero = Hero("Maxwell")
    goblins = [Goblin(f"Goblin {i+1}") for i in range(5)]
    defeated_goblins = 0
    total_damage_dealt = 0
    round_of_game = 0

    while hero.is_alive() and any(g.is_alive() for g in goblins):
        print("\nNew Round!")

        # Hero's turn
        target_goblin = random.choice([g for g in goblins if g.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        total_damage_dealt += damage
        target_goblin.take_damage(damage)

        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

        round_of_game += 1
        print("BOSS BANDIT HAS ENTERED THE ARENA!")

        boss_bandit = BOSS_BANDIT("Boss Bandit")
        while boss_bandit.is_alive() and hero.is_alive():
            damage = hero.strike()
            print(f"Hero attacks {boss_bandit.name} for {damage} damage!")
            total_damage_dealt += damage
            boss_bandit.take_damage(damage)

            if not boss_bandit.is_alive():
                print(f"{boss_bandit.name} has been defeated!")
                break

            damage = boss_bandit.attack()
            print(f"{boss_bandit.name} attacks hero for {damage} damage!")
            hero.receive_damage(damage)

            dash_damage = boss_bandit.dash()
            if dash_damage:
                print(
                    f"{boss_bandit.name} dashes and deals {dash_damage} damage!"
                )
                hero.receive_damage(dash_damage)

        print(f"End of Round {round_of_game}. Hero's health: {hero.health}")

    print(f"There were {round_of_game} rounds in this game.")

    if hero.is_alive():
        if boss_bandit.is_alive() is False:
            print("THE BOSS BANDIT HAS BEEN DEFEATED!")
        else:
            print("THE BOSS BANDIT IS STILL ALIVE!")
        print("\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print("\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    print("\nBattle Summary:" +
               f"\nTotal damage dealt by hero: {total_damage_dealt}" +
               f"\nRounds Survived: {round_of_game}")

    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")


if __name__ == "__main__":
    main()
