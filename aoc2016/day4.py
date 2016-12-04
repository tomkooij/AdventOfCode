def parse(string):
    name, checksum = string.split('[')
    checksum = checksum[:-1]  # remove ] bracket
    name, code = name.rsplit('-', 1)
    return name.replace('-', ''), code, checksum


def get_sector_id(string):
    """return sector ID if checksum matches, else return 0"""

    name, code, checksum = parse(string)

    # letter_count = [('a', 5), ('c', 4), ('x', 1), ('y', 1)]
    letter_count = list({(char, name.count(char)) for char in name})
    letter_count.sort()   # sort by letter
    letter_count.sort(key=lambda x: x[1], reverse=True)  # sort by count

    calculated_checksum = "".join([letter for letter, count in letter_count])
    if calculated_checksum[:5] == checksum:
        return int(code)
    else:
        return 0

with open('input/input4.txt') as f:
    sector_ids = [get_sector_id(line.rstrip('\n')) for line in f.readlines()]
    print(sum(sector_ids))
