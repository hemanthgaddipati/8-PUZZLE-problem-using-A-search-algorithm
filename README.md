# 8-PUZZLE-problem-using-A-search-algorithm
8-PUZZLE problem using A* search algorithm

# AIM:
To solve 8-puzzle problem using A* algorithm.

# PROBLEM STATEMENT:
Implement A* search algorithm and apply it to 8-puzzle problem. In addition to it provide
problem formulation, operators, g-cost and two heuristic functions (h-cost) of the 8-puzzle
problem.

# 8- PUZZLE PROBLEM:
The 8-puzzle consists of a 3x3 (3 by 3) grid area with 8 square blocks. Every single grid with that
in the puzzle is known as a tile, and there is a number ranging from 1 to 8 for each tile, so that
they are uniquely recognizable. The objective is to arrange the tiles according to the order
specified. The only way the blocks can move is either horizontally or vertically into a blank
square.

# PROBLEM FORMULATION:
Goal: Goal State is initially given.
States: Integer locations of tiles.
Actions: Move the blank tile UP, DOWN, LEFT or RIGHT.
Performance: Number of total moves in the solution

# A* ALGORITHM:
A * search algorithm is used to solve this puzzle which illustrates a general artificial intelligence
methodology. It is an informed search algorithm which is used in path findings and graph
traversals. It is a combination of uniform cost search (UCS) and best first search (greedy), which
avoids expanding expensive paths. A* star uses admissible heuristics which is optimal as it
avoids over-estimating the path to goal state. The evaluation function A* uses for calculating
the distance is:

f(n) = g(n) + h(n) where
g(n) = cost so far to reach n,
h(n) = estimated cost from n to goal,
f(n) = estimated total cost of path through n to goal

# Heuristic Functions:
The heuristic function is a way to inform the search regarding the direction to a goal. It provides
an information to estimate which neighboring node will lead to the goal. The two heuristic
functions that we considered for solving 8-puzzle problem are:

  ● Manhattan Distance: The distance between two tiles measured along the axes of
right angles. It is the sum of absolute values of differences between goal state (i, j)
coordinates and current state (l, m) coordinates respectively, i.e. |i - l|+ |j - m|
  ● Misplaced Tile: This calculates the number of misplaced tiles in any given state.

