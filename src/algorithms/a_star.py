import heapq
import math

WALL = '@'


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

def astar(array, start, end, width):

    """

    Args:
        array: two dimensional list with characters representing walls and floor - remember to adjust the wall constant
        start:
        end:
        width: height and width of the map in pixels (rows and colums) - only square arrays should be used

    Returns: cheapest path between start and goal found by A* algorithm utilizing euclidean heuristic - none if no path

    """

    # Allow for diagonal movement
    movements = [(1,  1),
                 (0, 1),
                 (0, -1),
                 (1, -1),
                 (-1, 1),
                 (-1,-1),
                 (1,  0),
                 (-1, 0)]

    # Set up
    open_set = []
    came_from = {}
    g_score = {start: 0}
    f_score = {start: euc_dist_heuristic(start, end)}
    heapq.heappush(open_set, (f_score[start], start))
    close_set = set()
    # Main loop
    while open_set:
        current = heapq.heappop(open_set)[1]

        # Goal found - collect and return the path
        if current == end:
            return reconstruct_path(start,came_from, current)

        # Add current to the visited node set and check the neighboring nodes
        close_set.add(current)
        for i, j in movements:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = g_score[current] + euc_dist_heuristic(current, neighbor)

            # Out of bounds conditions and wall check
            if 0 <= neighbor[0] < width:
                if 0 <= neighbor[1] < width:
                    if array[neighbor[0]][neighbor[1]] == WALL:
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= g_score.get(neighbor, 0):
                continue

            # Part of the cheapest path. Record the precedence and push the neighbor to queue
            if tentative_g_score < g_score.get(neighbor, 0) or neighbor not in [m[1] for m in open_set]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + euc_dist_heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))