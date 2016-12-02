# adventofcode.com
# day22

INPUTFILE = 'input/input22'



if __name__ == '__main__':
	with open(INPUTFILE) as f:
		_, _, input_boss_hp = f.readline().split()
		_, input_boss_damage = f.readline().split()
