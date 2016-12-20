with open('input\input20.txt') as f:
    ranges = [tuple(map(int, line.split('-'))) for line in f.readlines()]
    ranges.sort()

max_begin, max_end = 0, 0
must_start_at = 0
gap = 0

breakpoints = []
for begin, end in ranges:

    if begin > must_start_at:
        """
        The next sorted range does not begin at the right value
        we have found a gap in the range
        """
        breakpoints.append(must_start_at)
        gap += begin - (max_end + 1)

    max_begin = max(begin, max_begin)
    max_end = max(end, max_end)

    if end > max_begin:
        """extend the range"""
        must_start_at = max(end + 1, max_end + 1)

print('part A: ', breakpoints[0])
print('part B: ', gap)
 
