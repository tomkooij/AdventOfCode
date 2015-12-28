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

    n = 1

    max_row, max_column = 1,1
    row, column = 1,1

    while 1:
        #print row, column, n
        if (row == ROW and column == COLUMN):
            break

        # go up-right
        column += 1
        row -= 1

        if row == 0:
            # next diagonal
            column = 1
            max_row += 1
            row = max_row
            #print "next diagnonal: max row = ", max_row

        n += 1
    return n


if __name__ == '__main__':

    for row, column, TESTCASE in INPUT:

        n = count_to(row, column)

        k = START * modular_pow(MUL, n-1, MOD) % MOD

        if TESTCASE is not None:
            assert k == TESTCASE, 'Testcase failure: (%d, %d) = %d' % (row, column, k)

        print "n (%d, %d) = %d" % (row, column, k)
