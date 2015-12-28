# adventofcode.com
# day25

START = 20151125
MOD = 33554393
MUL = 252533

# row, column, answer. Answer is not None => testcase
INPUT = [(2, 2, 21629792), (6, 6, 27995004), (2978, 3083, None)]


def modular_pow(base, exponent, modulus):
    """ pseudocode from: https://en.wikipedia.org/wiki/Modular_exponentiation
        which quotes B. Schneier, Applied Cryptography as source """

    if modulus == 1: return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result % modulus


def count_to(ROW, COLUMN):
    """count the number of iterations from (1,1) to (ROW, COLUMN)"""
    n = 0

    # n = 1 + 2 + 3 + ...
    for diagonal in xrange(1, ROW+COLUMN):
        n += diagonal
        
    return n - (ROW - 1)


if __name__ == '__main__':

    for row, column, TESTCASE in INPUT:

        n = count_to(row, column)

        k = START * modular_pow(MUL, n-1, MOD) % MOD

        if TESTCASE is not None:
            assert k == TESTCASE, 'Testcase failure: n = %d (%d, %d) = %d' % (n, row, column, k)

        print "n = %d (%d, %d) = %d" % (n, row, column, k)
