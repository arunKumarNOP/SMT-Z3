from __future__ import print_function
from z3 import *
import time


def solve(puzzle):
    # init the cells of sudoku
    cell = [[Int('cell{0}{1}'.format(i, j)) for j in range(9)] for i in range(9)]

    #init the solver
    s = Solver()

    k = 0
    for i in range(9):
        for j in range(9):
            # set the appropriate cell with constant
            if puzzle[k] != '.':
                s.add(cell[i][j] == int(puzzle[k]))
            else:
                # constrain for each cell, we want numbers in 1-9 range only
                # why not add this for all cells? - in the above if statement we already fixed
                # a constant, for those cases we need not add this range constraint
                # Result - Less constraint less solving time
                s.add(cell[i][j] >= 1)
                s.add(cell[i][j] <= 9)
            k = k + 1

    for i in range(9):

        # constrain for each row
        s.add(Distinct(cell[i][0],
                       cell[i][1],
                       cell[i][2],
                       cell[i][3],
                       cell[i][4],
                       cell[i][5],
                       cell[i][6],
                       cell[i][7],
                       cell[i][8]))

        #constrain for each column
        s.add(Distinct(cell[0][i],
                       cell[1][i],
                       cell[2][i],
                       cell[3][i],
                       cell[4][i],
                       cell[5][i],
                       cell[6][i],
                       cell[7][i],
                       cell[8][i]))

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s.add(Distinct(cell[i+0][j], cell[i+0][j+1], cell[i+0][j+2],
                           cell[i+1][j], cell[i+1][j+1], cell[i+1][j+2],
                           cell[i+2][j], cell[i+2][j+1], cell[i+2][j+2]))

    if s.check() == sat:
        m = s.model()

        for i in range(9):
            for j in range(0, 9, 3):
                print(str(m[cell[i][j]]) + ' ' + str(m[cell[i][j+1]]) + ' ' + str(m[cell[i][j+2]]),end='   ')
            print()
            if (i+1) % 3 == 0:
                print()

# http://www.7sudoku.com/view-puzzle?date=20161025
puzzle = '.7.5....4.....698.6....42.7.....2.9.3.4.9.7.2.9.1.....9.84....5.356.....7....8.4.'

if __name__ == '__main__':
    solve(puzzle)
    