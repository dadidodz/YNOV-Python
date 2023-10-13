from spaceships import BattleshipKiller, FighterKiller, Interceptor, Bomber, Destroyer

if __name__ == '__main__':
    killer = BattleshipKiller()
    print(killer.attack)

    bomber = Bomber()
    print(bomber.attack)

    destroyer = Destroyer()
    print(destroyer.attack)

    fighter = FighterKiller()
    print(fighter.attack)