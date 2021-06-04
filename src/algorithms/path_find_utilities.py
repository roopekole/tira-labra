import math

WALL = '@'
MOVEMENTS = [(1,  1),
             (0, 1),
             (0, -1),
             (1, -1),
             (-1, 1),
             (-1,-1),
             (1,  0),
             (-1, 0)]


def reconstruct_path(start,came_from,current):
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


def block(current_x, current_y, direction_x, direction_y, array):
    if current_x + direction_x < 0 or current_x + direction_x >= len(array):
        return True
    if current_y + direction_y < 0 or current_y + direction_y >= len(array):
        return True
    if direction_x != 0 and direction_y != 0:
        if array[current_x + direction_x][current_y] == WALL and array[current_x][current_y + direction_y] == WALL:
            return True
        if array[current_x + direction_x][current_y + direction_y] == WALL:
            return True
    else:
        if direction_x != 0:
            if array[current_x + direction_x][current_y] == WALL:
                return True
        else:
            if array[current_x][current_y + direction_y] == WALL:
                return True
    return False