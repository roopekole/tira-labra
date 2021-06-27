#!/usr/bin/python3

import a_star
import jps

map = [[".", ".", ".", ".", "."],
       [".", "@", "@", "@", "."],
       [".", "@", ".", "@", "."],
       [".", "@", "@", ".", "."],
       [".", ".", ".", ".", "."]]
start = (2, 2)
goal = (0, 0)


print("Dikstra", a_star.astar(map, start, goal, 0))
print("A*", a_star.astar(map, start, goal, 1))
route = jps.jps(map, start, goal)
print("JPS", route)
