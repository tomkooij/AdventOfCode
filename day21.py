# adventofcode.com
# day21

#input
boss_hp =  104
boss_damage = 8
boss_armor = 1

def player_wins(player, boss):
    """ return True if player wins """

    player_survives_rounds = player['hp'] / max(1,boss['damage'] - player['armor'])
    boss_survives_rounds = boss['hp'] / max(1,player['damage'] - boss['armor'])

    return player_survives_rounds >= boss_survives_rounds

def set_stats(hp=100, damage=1, armor=1):
    return {'hp':hp, 'damage':damage, 'armor':armor}

if __name__ == '__main__':
    player = set_stats(hp=8, damage=5, armor=5)
    boss = set_stats(hp=12, damage=7, armor=2)
    assert player_wins(player, boss), 'Testcase failure!'

    boss = set_stats(hp=boss_hp, damage=boss_damage, armor=boss_armor)
    
