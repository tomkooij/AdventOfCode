from collections import defaultdict

chip1, chip2 = 17, 61
bots = defaultdict(list)
output = {}


def parse(line):
    """parse and execute a line. If not possible return False"""

    cmd, *rest = line.split()
    if cmd == 'value':
        # value 5 goes to bot 2
        chipnumber = int(rest[0])
        botno = int(rest[4])
        bots[botno].append(chipnumber)
    if cmd == 'bot':
        giving_botno = int(rest[0])
        if len(bots[giving_botno]) != 2:
            return False
        else:
            # bot 2 gives low to bot 1 and high to bot 0
            botno = int(rest[5])
            chipnumber = min(bots[giving_botno])
            if rest[4] == 'bot':
                bots[botno].append(chipnumber)
            else:
                output[botno] = chipnumber
            botno = int(rest[10])
            chipnumber = max(bots[giving_botno])
            if rest[9] == 'bot':
                bots[botno].append(chipnumber)
            else:
                output[botno] = chipnumber
    return True


with open('input\input10.txt') as f:
    queue = [line.rstrip('\n') for line in f.readlines()]
    while queue:
        line = queue.pop(0)
        if not parse(line):
            queue.append(line)

for key, value in bots.items():
    if chip1 in value and chip2 in value:
        print("Bot %d has chips %d and %d" % (key, chip1, chip2))

print("part B: ", output[0]*output[1]*output[2])
