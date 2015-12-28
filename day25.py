# adventofcode.com
# day25

START = 20151125
MOD = 33554393
MUL = 252533

ROW = 2978
COLUMN = 3083

def f(n):
    return n * MUL % MOD

if __name__ == '__main__':

    n = START

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

        n = f(n)
    print "n (%d, %d) = %d" % (row, column, n)
