#!/usr/bin/python3
from src.algorithms import a_star, jps, a_star_min_heap

map = [[".", ".", ".", ".", "."],
               [".", "@", "@", "@", "."],
               [".", "@", ".", "@", "."],
               [".", "@", "@", ".", "."],
               [".", ".", ".", ".", "."]]
start = (2,2)
goal = (0,0)



print("Dikstra",a_star.astar(map,start, goal, 0))
print("A*",a_star.astar(map,start, goal, 1))
print("A*",a_star_min_heap.astar(map,start, goal, 1))
route=jps.jps(map,start, goal)
print("JPS",route)
