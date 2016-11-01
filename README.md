# My SMT Projects using Z3

# 1. Sudoku solver
Solves any level sudoku

Input puzzle ex:-

'.7.5....4.....698.6....42.7.....2.9.3.4.9.7.2.9.1.....9.84....5.356.....7....8.4.'<br>
(Taken from http://www.7sudoku.com/view-puzzle?date=20161025)

Soln:<br>
<pre>2 7 9   5 8 3   1 6 4
5 4 1   7 2 6   9 8 3
6 8 3   9 1 4   2 5 7

1 5 7   3 6 2   4 9 8
3 6 4   8 9 5   7 1 2
8 9 2   1 4 7   5 3 6

9 2 8   4 3 1   6 7 5
4 3 5   6 7 9   8 2 1
7 1 6   2 5 8   3 4 9 </pre>

# 2. Queen Problem
Solves 8 queen problem using Z3, extended to n-queen problem.
<br>
Currently prints only one solution but can be extended to print all solution.

Soln for 8-queen problem:<br>
<pre>0 0 1 0 0 0 0 0 
0 0 0 0 1 0 0 0 
0 1 0 0 0 0 0 0 
0 0 0 0 0 0 0 1 
1 0 0 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 0 1 0 0 0 0 
0 0 0 0 0 1 0 0 </pre>
