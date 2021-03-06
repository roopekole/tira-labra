#!/usr/bin/python3
import math

WALL = '@'
MOVEMENTS = [(1,  1),
             (0, 1),
             (0, -1),
             (1, -1),
             (-1, 1),
             (-1, -1),
             (1,  0),
             (-1, 0)]


def reconstruct_path(start, came_from, current):
    """

    Args:
        start: start coordinates
        came_from: precedent node of the current node on the cheapest path
        current: current node, iteration begins with the target node

    Returns: cheapest path reversed relative to the iteration (start to end)

    """
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(start)
    return path[::-1]


def euc_dist_heuristic(p1, p2):
    """

    Args:
        p1:
        p2:

    Returns: euclidean distance between the points p1 and p2

    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def block(current_x, current_y, direction_x, direction_y, graph):
    """

    Args:
        current_x: Current x-coordinate
        current_y: Current y-coordinate
        direction_x: increment to x coordinate
        direction_y: increment to y coordinate
        graph: 2d graph

    Returns: True if the evaluated location (given by the current coordinates with incremented
            direction) is out of bounds or an obstacle (wall).

    """
    new_x = current_x + direction_x
    new_y = current_y + direction_y

    if new_x < 0 or new_x >= len(graph) or new_y < 0 or new_y >= len(graph):
        return True

    if graph[new_x][new_y] == WALL:
        return True

    return False
