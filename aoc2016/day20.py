def solve(ranges, partA=False):
    max_begin, max_end = 0, 0
    total_gap = 0

    for begin, end in sorted(ranges):

        gap = begin - (max_end + 1)
        if gap > 0:
            """we have found a gap in the range"""
            if partA:
                return max_end + 1
            total_gap += gap

        max_begin = max(begin, max_begin)
        max_end = max(end, max_end)

    return total_gap


with open('input\input20.txt') as f:
    ranges = [tuple(map(int, line.split('-'))) for line in f.readlines()]

print('part A: ', solve(ranges, partA=True))
print('part B: ', solve(ranges))
