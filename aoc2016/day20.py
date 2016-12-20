

with open('input\input20.txt') as f:
    ranges = [tuple(map(int, line.split('-'))) for line in f.readlines()]
    ranges.sort()


max_begin, max_end = 0, 0
must_start_at = 0
n = 0
for idx, (begin, end) in enumerate(ranges):
    if begin > must_start_at:
        print('found!' , idx, begin, end, max_begin, max_end)
        n += begin-(max_end+1)
    print (idx, begin, end)
    max_begin = max(begin, max_begin)
    max_end = max(end, max_end)

    if end > max_begin:
        must_start_at = max(end+1, max_end+1)

print(n)
