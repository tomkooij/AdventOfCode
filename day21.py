# adventofcode.com
# day21

from itertools import combinations, product
from collections import defaultdict

#input
boss_hp =  104
boss_damage = 8
boss_armor = 1

Weapons = [
	("Dagger",      8, 4, 0),
	("Shortsword", 10, 5, 0),
	("Warhammer",  25, 6, 0),
	("Longsword",  40, 7, 0),
	("Greataxe",   74, 8, 0) ]

Armor = [
    ("Naked", 0, 0, 0),
    ("Leather",     13, 0, 1),
	("Chainmail",   31, 0, 2),
	("Splintmail",  53, 0, 3),
	("Bandedmail",  75, 0, 4),
	("Platemail",  102, 0, 5) ]

Rings = [
    ("No ring", 0, 0, 0),
    ("Damage +1",   25, 1, 0),
	("Damage +2",   50, 2, 0),
	("Damage +3",  100, 3, 0),
	("Defense +1",  20, 0, 1),
	("Defense +2",  40, 0, 2),
	("Defense +3",  80, 0, 3) ]


def player_wins(player, boss):
    """ return True if player wins """

    while player['hp'] > 0 :
        boss['hp'] -= max(1,player['damage'] - boss['armor'])
        if boss['hp'] <= 0:
            return True
        player['hp'] -= max(1,boss['damage'] - player['armor'])

    return False


def set_stats(hp=100, damage=1, armor=1):
    return {'hp':hp, 'damage':damage, 'armor':armor}


if __name__ == '__main__':
    player = set_stats(hp=8, damage=5, armor=5)
    boss = set_stats(hp=12, damage=7, armor=2)
    assert player_wins(player, boss), 'Testcase failure!'

    player = defaultdict(int)
    boss = defaultdict(int)
    player['hp'] = 100
    boss['hp'] = boss_hp
    boss['damage'] = boss_damage
    boss['armor'] = boss_armor

    solutionA = []
    solutionB = []

    for stats in product(Weapons, Armor, Rings, Rings):
        player['hp'] = 100
        player['cost'] = 0
        player['damage'] = 0
        player['armor'] = 0
        boss['hp'] = boss_hp
        boss['damage'] = boss_damage
        boss['armor'] = boss_armor

        for stat in stats:
            player['cost'] += stat[1]
            player['damage'] += stat[2]
            player['armor'] += stat[3]

        if player_wins(player, boss):
            solutionA.append(player['cost'])
        else:
            solutionB.append(player['cost'])

    print 'part A', min(solutionA)
    print 'part B', max(solutionB)
