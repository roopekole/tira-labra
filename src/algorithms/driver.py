from src.algorithms.a_star import astar
map = [["@", "@", "@", "@", "@"],
       ["@", ".", "@", ".", "@"],
       ["@", ".", "@", ".", "@"],
       ["@", ".", ".", ".", "@"],
       ["@", "@", "@", "@", "@"]]
print(len(map))

x_coords = []
y_coords = []
start = (1,1)
goal = (1,3)
route = astar(map, start, goal, len(map))
route = route
print(route)
