def sort_words_in_list(l):
    return [sort_word(i) for i in l]


def sort_word(s):
    return ''.join(sorted(list(s)))


with open('input/input04.txt') as f:

    rows = [line.split() for line in f.readlines()]
    print('part a', sum([len(row)==len(set(row))
                         for row in rows]))
    print('part b', sum([len(row)==len(set(sort_words_in_list(row)))
                         for row in rows]))
