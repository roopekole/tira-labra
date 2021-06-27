#!/usr/bin/python3
import time
from src.data_structures.heap import Heap
from src.algorithms.path_find_utilities import MOVEMENTS, reconstruct_path, euc_dist_heuristic, block


def jps(graph, start, end):
    """

    Args:
        graph: two dimensional list with characters representing walls and floor - remember to adjust the wall constant
        start:
        end:

    Returns:cheapest path between start and goal found by JPS algorithm utilizing euclidean heuristic - none if no path.
            Also return the runtime in milliseconds and iterations (triple)

    """

    # Similar set-up as in A star algorithm
    current_time = round(time.time() * 1000)
    iterations = 0

    open_set = Heap()
    came_from = {}
    close_set = set()
    g_score = {start: 0}
    f_score = {start: euc_dist_heuristic(start, end)}

    open_set.push((f_score[start], start))

    while open_set.size > -1:
        current = open_set.pop()[1]
        if current == end:
            path = reconstruct_path(start, came_from, current)
            runtime = round(time.time() * 1000) - current_time
            return get_full_path(path), runtime, iterations

        iterations += 1
        close_set.add(current)

        # List of jump points after neighbor pruning
        jump_points = []

        neighbors = get_neighbors(current[0], current[1], came_from.get(
        (current[0], current[1]), 0), graph)

        for neighbor in neighbors:
            direction_x, direction_y = get_direction(neighbor[0], neighbor[1], current[0], current[1])
            
            jump_point = jump(current[0], current[1], direction_x,
                            direction_y, graph, end)

            if jump_point is not None:
                jump_points.append(jump_point)

        for jump_point in jump_points:

            if jump_point in close_set and tentative_g_score >= g_score.get(jump_point, 0):
                continue

            tentative_g_score = g_score[current] + \
                euc_dist_heuristic(current, jump_point)

            # Part of the cheapest path. Record the precedence and push the jump point to queue
            if tentative_g_score < g_score.get(jump_point, 0) or jump_point not in [jp[1] for jp in open_set.heap]:
                came_from[jump_point] = current
                g_score[jump_point] = tentative_g_score
                f_score[jump_point] = tentative_g_score + \
                    euc_dist_heuristic(jump_point, end)
                open_set.push((f_score[jump_point], jump_point))


def get_full_path(path):
    """

    Args:
        path: takes the path given by the jump points

    Returns: returns the full path with skipped points between the jump points.

    """
    full_path = [path[0]]

    for i in range(len(path)):
        # Iterate each jump point
        if i < len(path) - 1:
            # Get the direction between the discovered jump paths
            direction = get_direction(
                path[i+1][0], path[i+1][1], path[i][0], path[i][1])
            # Skipped points are the pruned symmetry points
            skipped_point = path[i][0] + \
                direction[0], path[i][1] + direction[1]

            # Append with euclidean straight line points until next jump point
            while skipped_point != path[i+1]:
                full_path.append(skipped_point)
                skipped_point = skipped_point[0] + \
                    direction[0], skipped_point[1] + direction[1]

            # Append with jump points until the last point
            if path[i+1] != path[-1]:
                full_path.append(path[i+1])

        # Append last jump point
        else:
            full_path.append(skipped_point)

    return full_path


def get_direction(current_x, current_y, previous_x, previous_y):
    """

    Args:
        current_x:
        current_y:
        previous_x:
        previous_y:

    Returns: (i,j) direction between the two x,y coordinates. i,j in [-1,0,1]

    """
    direction_x = bool(current_x - previous_x > 0) - \
        bool(current_x - previous_x < 0)
    direction_y = bool(current_y - previous_y > 0) - \
        bool(current_y - previous_y < 0)

    return direction_x, direction_y


def get_neighbors(current_x, current_y, parent, graph):
    """

    Args:
        current_x:
        current_y:
        parent: Jump point / neighboring parent of the current node tuple
        graph:

    Returns: A list of valid neighbors for the current node represented by x,y tuple.

    """
    neighbors = []
    # If clause for a first node in the queue which is an 'int' instead of tuple
    if type(parent) == int:
        for i, j in MOVEMENTS:
            if not block(current_x, current_y, i, j, graph):
                neighbors.append((current_x + i, current_y + j))
        return neighbors

    # Compute the direction of movement
    direction_x, direction_y = get_direction(
        current_x, current_y, parent[0], parent[1])

    # Neighbors along the diagonal movement
    if direction_x != 0 and direction_y != 0:
        
        # Forced neighbor condition (see: https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search.html)
        if block(current_x, current_y, -direction_x, 0, graph) and not block(
            current_x, current_y, 0, direction_y, graph):
            neighbors.append((current_x - direction_x, current_y + direction_y))
        if block(current_x, current_y, 0, -direction_y, graph) and not block(
            current_x, current_y, direction_x, 0, graph):
            neighbors.append((current_x + direction_x, current_y - direction_y))

        # Vertical neighbor
        if not block(current_x, current_y, 0, direction_y, graph):
            neighbors.append((current_x, current_y + direction_y))
        # Horizontal neighbor
        if not block(current_x, current_y, direction_x, 0, graph):
            neighbors.append((current_x + direction_x, current_y))
        # Diagonal neighbor
        if (not block(current_x, current_y, 0, direction_y, graph)
            or not block(current_x, current_y, direction_x, 0, graph)
            ) and not block(current_x, current_y, direction_x, direction_y, graph):
            neighbors.append((current_x + direction_x, current_y + direction_y))

    else:
        # Neighbors along the vertical movement
        if direction_x == 0:
            if not block(current_x, current_y, direction_x, 0, graph):
                if not block(current_x, current_y, 0, direction_y, graph):
                    neighbors.append((current_x, current_y + direction_y))
                if block(current_x, current_y, 1, 0, graph):
                    neighbors.append((current_x + 1, current_y + direction_y))
                if block(current_x, current_y, -1, 0, graph):
                    neighbors.append((current_x - 1, current_y + direction_y))

        else:
            # Neighbors along the horizontal movement
            if not block(current_x, current_y, direction_x, 0, graph):
                if not block(current_x, current_y, direction_x, 0, graph):
                    neighbors.append((current_x + direction_x, current_y))
                if block(current_x, current_y, 0, 1, graph):
                    neighbors.append((current_x + direction_x, current_y + 1))
                if block(current_x, current_y, 0, -1, graph):
                    neighbors.append((current_x + direction_x, current_y - 1))
    return neighbors


def jump(current_x, current_y, direction_x, direction_y, graph, end):
    """
    This method attempts to prune the symmetry on the graph by eliminating identical cost paths
    and by identifying the interesting jump points.

    Args:
        current_x:
        current_y:
        direction_x:
        direction_y:
        graph:
        end:

    Returns: A jump point for which the symmetry pruning has occurred
    """

    # New coordinates
    new_x = current_x + direction_x
    new_y = current_y + direction_y
    
    if block(new_x, new_y, 0, 0, graph):
        return None

    if (new_x, new_y) == end:
        return new_x, new_y

    # Coordinates that pruned until jump point
    valid_new_x = new_x
    valid_new_y = new_y

    # Diagonal jump, eliminate diagonal symmetry
    if direction_x != 0 and direction_y != 0:
        while True:
            if (not block(valid_new_x, valid_new_y, -
                          direction_x, direction_y, graph)
                and block(valid_new_x, valid_new_y, -direction_x, 0, graph)
                or not block(valid_new_x, valid_new_y, direction_x, -direction_y, graph)
                and block(valid_new_x, valid_new_y, 0, -direction_y, graph)):
                
                return valid_new_x, valid_new_y

            # Recursive vertical and horizontal expansion of the diagonal pruning
            if (jump(valid_new_x, valid_new_y, direction_x, 0, graph, end) is not None
                    or jump(valid_new_x, valid_new_y, 0, direction_y, graph, end) is not None):
                return valid_new_x, valid_new_y

            # Move further along the diagonal direction
            valid_new_x += direction_x
            valid_new_y += direction_y

            if block(valid_new_x, valid_new_y, 0, 0, graph):
                return None

            if (valid_new_x, valid_new_y) == end:
                return valid_new_x, valid_new_y
    else:
        # Horizontal jump, prune the horizontal symmetry until a jump point is reached
        if direction_x != 0:
            while True:
                if (
                    not block(valid_new_x, new_y, direction_x, 1, graph)
                    and block(valid_new_x, new_y, 0, 1, graph)
                    or not block(valid_new_x, new_y, direction_x, -1, graph)
                    and block(valid_new_x, new_y, 0, -1, graph)
                ):
                    return valid_new_x, new_y

                # Move further along the horizontal line
                valid_new_x += direction_x

                if block(valid_new_x, new_y, 0, 0, graph):
                    return None

                if (valid_new_x, new_y) == end:
                    return valid_new_x, new_y

        else:
            # Vertical jump, prune the vertical symmetry until a jump point is reached
            while True:
                if (
                    not block(new_x, valid_new_y, 1, direction_y, graph)
                    and block(new_x, valid_new_y, 1, 0, graph)
                    or not block(new_x, valid_new_y, -1, direction_y, graph)
                    and block(new_x, valid_new_y, -1, 0, graph)
                ):
                    return new_x, valid_new_y

                # Move further along the vertical line
                valid_new_y += direction_y

                if block(new_x, valid_new_y, 0, 0, graph):
                    return None

                if (new_x, valid_new_y) == end:
                    return new_x, valid_new_y
