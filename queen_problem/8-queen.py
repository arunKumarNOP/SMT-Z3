from __future__ import print_function
from z3 import *


def add(a, b):
    return a+b


def solve():
    # init the cells
    cell = [[Int('cell{0}{1}'.format(i, j)) for j in range(8)] for i in range(8)]

    # init the solver
    s = Solver()

    s.add(reduce(lambda a, b: a+b, [cell[i][j] for j in range(8) for i in range(8)]) == 8)

    for i in range(8):
        for j in range(8):
            s.add(cell[i][j] >= 0)
            s.add(cell[i][j] <= 1)

    for i in range(8):
        s.add(reduce(add, cell[i]) <= 1)
        s.add(reduce(add, [row[i] for row in cell]) <= 1)

    # Add constraint for diagonals
    for k in range(8):
        # top right diagonal from (0,k) to (7-k,7)
        diagTR = reduce(add, [cell[i - k][i] for i in range(k, 8)])

        # bottom left diagonal from (k,0) to (7,7-k)
        diagBL = reduce(add, [cell[i][i - k] for i in range(k, 8)])

        # top left diagonal from (0,k) to (k,0)
        diagTL = reduce(add, [cell[i][k - i] for i in range(k + 1)])

        # bottom right diagonal from (7,k) to (k,7)
        diagBR = reduce(add, [cell[7 - i][7 - k + i] for i in range(k + 1)])

        s.add(diagTR <= 1)
        s.add(diagBL <= 1)
        s.add(diagTL <= 1)
        s.add(diagBR <= 1)

    if s.check() == sat:
        m = s.model()
        for i in range(8):
            for j in range(8):
                print(m[cell[i][j]], end=' ')
            print()

if __name__ == '__main__':
    solve()