from __future__ import print_function
from z3 import *


def add(a, b):
    return a+b


def solve(n):
    # init the cells
    cell = [[Int('cell{0}{1}'.format(i, j)) for j in range(n)] for i in range(n)]

    # init the solver
    s = Solver()

    # there must be n queen on the board
    s.add(reduce(lambda a, b: a+b, [cell[i][j] for j in range(n) for i in range(n)]) == n)
    
    # 1 denotes a queen 0 denotes empty cell
    for i in range(n):
        for j in range(n):
            s.add(cell[i][j] >= 0)
            s.add(cell[i][j] <= 1)
    
    # Constraint for one queen in a row and a column
    for i in range(n):
        s.add(reduce(add, cell[i]) <= 1)
        s.add(reduce(add, [row[i] for row in cell]) <= 1)

    # Add constraint for diagonals
    for k in range(n):
        # top right diagonal from (0,k) to (n-1-k,n-1)
        diagTR = reduce(add, [cell[i - k][i] for i in range(k, n)])

        # bottom left diagonal from (k,0) to (n-1,n-1-k)
        diagBL = reduce(add, [cell[i][i - k] for i in range(k, n)])

        # top left diagonal from (0,k) to (k,0)
        diagTL = reduce(add, [cell[i][k - i] for i in range(k + 1)])

        # bottom right diagonal from (n-1,k) to (k,n-1)
        diagBR = reduce(add, [cell[n - 1 - i][n - 1 - k + i] for i in range(k + 1)])

        s.add(diagTR <= 1)
        s.add(diagBL <= 1)
        s.add(diagTL <= 1)
        s.add(diagBR <= 1)

    if s.check() == sat:
        m = s.model()
        for i in range(n):
            for j in range(n):
                print(m[cell[i][j]], end=' ')
            print()

if __name__ == '__main__':
    solve(8)