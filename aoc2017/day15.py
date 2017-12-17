def generator_partA(start, multiplication_factor, N=5):
    x = start
    for _ in range(N):
        x *= multiplication_factor
        x %= 2147483647
        yield x
        
def generator_partB(start=0, multiplication_factor=1, div=1, N=1000):
    x = start
    while N > 0:
        x *= multiplication_factor
        x %= 2147483647
        if not x % div:
            N -= 1
            yield x
        
def solve(genA, genB, N):
    duplicates = 0
    for a, b in zip(genA, genB):
        if (a & 0xFFFF == b & 0xFFFF):
            duplicates += 1
    return duplicates


N = 40 * int(1e6)
genA = generator_partA(start=634, multiplication_factor=16807, N=N)
genB = generator_partA(start=301, multiplication_factor=48271, N=N)
print('part a:', solve(genA, genB, N))

N = 5 * int(1e6)
genA = generator_partB(start=634, multiplication_factor=16807, div=4, N=N)
genB = generator_partB(start=301, multiplication_factor=48271, div=8, N=N)
print('part b:', solve(genA, genB, N))
