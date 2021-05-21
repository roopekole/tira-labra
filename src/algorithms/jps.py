import sys
from src.data_structures import graph


def jps(start_x, start_y, end_x, end_y, map):
    print(map)
    return map

path = sys.path[1] + "/example/" + "Berlin_0_256" + ".map"
with open(path, "r") as map:
    data = map.read().splitlines()

