import time, heapq
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
    current_time = round(time.time() * 1000)
    iterations = 0

    open_set = []
    came_from = {}
    close_set = set()
    g_score = {start: 0}
    f_score = {start: euc_dist_heuristic(start, end)}

    heapq.heappush(open_set, (f_score[start], start))

    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == end:
            path = reconstruct_path(start, came_from, current)
            runtime = round(time.time() * 1000) - current_time
            return get_full_path(path), runtime, iterations

        iterations += 1
        close_set.add(current)

        successors = get_successors(graph, current[0], current[1], came_from, end)

        for successor in successors:
            jump_point = successor

            if jump_point in close_set and tentative_g_score >= g_score.get(jump_point, 0):
                continue

            tentative_g_score = g_score[current] + euc_dist_heuristic(current, jump_point)

            # Part of the cheapest path. Record the precedence and push the jump point to queue
            if tentative_g_score < g_score.get(jump_point, 0) or jump_point not in [jp[1] for jp in open_set]:
                came_from[jump_point] = current
                g_score[jump_point] = tentative_g_score
                f_score[jump_point] = tentative_g_score + euc_dist_heuristic(jump_point, end)
                heapq.heappush(open_set, (f_score[jump_point], jump_point))


def get_full_path(path):
    """

    Args:
        path: takes the path given by the jump points

    Returns: returns the full path with skipped points between the jump points.

    """
    full_path = [path[0]]

    for i in range(len(path)):
        if i < len(path) - 1:
            direction = get_direction(path[i+1][0], path[i+1][1],path[i][0], path[i][1])
            skipped_point = path[i][0] + direction[0], path[i][1] + direction[1]

            while skipped_point != path[i+1]:
                full_path.append(skipped_point)
                skipped_point = skipped_point[0] + direction[0], skipped_point[1] + direction[1]
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
    direction_x = bool(current_x - previous_x > 0) - bool(current_x - previous_x < 0)
    direction_y = bool(current_y - previous_y > 0) - bool(current_y - previous_y < 0)

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
    if type(parent) != tuple:
        for i, j in MOVEMENTS:
            if not block(current_x, current_y, i, j, graph):
                neighbors.append((current_x + i, current_y + j))

        return neighbors
    direction_x, direction_y = get_direction(current_x, current_y, parent[0], parent[1])

    if direction_x != 0 and direction_y != 0:
        if not block(current_x, current_y, 0, direction_y, graph):
            neighbors.append((current_x, current_y + direction_y))
        if not block(current_x, current_y, direction_x, 0, graph):
            neighbors.append((current_x + direction_x, current_y))
        if (
            not block(current_x, current_y, 0, direction_y, graph)
            or not block(current_x, current_y, direction_x, 0, graph)
        ) and not block(current_x, current_y, direction_x, direction_y, graph):
            neighbors.append((current_x + direction_x, current_y + direction_y))
        if block(current_x, current_y, -direction_x, 0, graph) and not block(
            current_x, current_y, 0, direction_y, graph
        ):
            neighbors.append((current_x - direction_x, current_y + direction_y))
        if block(current_x, current_y, 0, -direction_y, graph) and not block(
            current_x, current_y, direction_x, 0, graph
        ):
            neighbors.append((current_x + direction_x, current_y - direction_y))

    else:
        if direction_x == 0:
            if not block(current_x, current_y, direction_x, 0, graph):
                if not block(current_x, current_y, 0, direction_y, graph):
                    neighbors.append((current_x, current_y + direction_y))
                if block(current_x, current_y, 1, 0, graph):
                    neighbors.append((current_x + 1, current_y + direction_y))
                if block(current_x, current_y, -1, 0, graph):
                    neighbors.append((current_x - 1, current_y + direction_y))

        else:
            if not block(current_x, current_y, direction_x, 0, graph):
                if not block(current_x, current_y, direction_x, 0, graph):
                    neighbors.append((current_x + direction_x, current_y))
                if block(current_x, current_y, 0, 1, graph):
                    neighbors.append((current_x + direction_x, current_y + 1))
                if block(current_x, current_y, 0, -1, graph):
                    neighbors.append((current_x + direction_x, current_y - 1))
    return neighbors


def get_successors(graph, current_x, current_y, came_from, goal):
    """

    Args:
        graph:
        current_x:
        current_y:
        came_from:
        goal:

    Returns: Returns the identified successors which cannot be reached by any alternative symmetric path

    """
    successors = []
    neighbours = get_neighbors(current_x, current_y, came_from.get((current_x, current_y), 0), graph)

    for n in neighbours:
        direction_x = n[0] - current_x
        direction_y = n[1] - current_y

        jump_point = jump(current_x, current_y, direction_x, direction_y, graph, goal)

        if jump_point is not None:
            successors.append(jump_point)

    return successors


def jump(current_x, current_y, direction_x, direction_y, graph, end):

    new_x = current_x + direction_x
    new_y = current_y + direction_y
    if block(new_x, new_y, 0, 0, graph):
        return None

    if (new_x, new_y) == end:
        return new_x, new_y

    valid_new_x = new_x
    valid_new_y = new_y

    if direction_x != 0 and direction_y != 0:
        while True:
            if (
                not block(valid_new_x, valid_new_y, -direction_x, direction_y, graph)
                and block(valid_new_x, valid_new_y, -direction_x, 0, graph)
                or not block(valid_new_x, valid_new_y, direction_x, -direction_y, graph)
                and block(valid_new_x, valid_new_y, 0, -direction_y, graph)
            ):
                return valid_new_x, valid_new_y

            if (jump(valid_new_x, valid_new_y, direction_x, 0, graph, end) is not None
                    or jump(valid_new_x, valid_new_y, 0, direction_y, graph, end) is not None):
                return valid_new_x, valid_new_y

            valid_new_x += direction_x
            valid_new_y += direction_y

            if block(valid_new_x, valid_new_y, 0, 0, graph):
                return None

            if (valid_new_x, valid_new_y) == end:
                return valid_new_x, valid_new_y
    else:
        if direction_x != 0:
            while True:
                if (
                    not block(valid_new_x, new_y, direction_x, 1, graph)
                    and block(valid_new_x, new_y, 0, 1, graph)
                    or not block(valid_new_x, new_y, direction_x, -1, graph)
                    and block(valid_new_x, new_y, 0, -1, graph)
                ):
                    return valid_new_x, new_y

                valid_new_x += direction_x

                if block(valid_new_x, new_y, 0, 0, graph):
                    return None

                if (valid_new_x, new_y) == end:
                    return valid_new_x, new_y

        else:
            while True:
                if (
                    not block(new_x, valid_new_y, 1, direction_y, graph)
                    and block(new_x, valid_new_y, 1, 0, graph)
                    or not block(new_x, valid_new_y, -1, direction_y, graph)
                    and block(new_x, valid_new_y, -1, 0, graph)
                ):
                    return new_x, valid_new_y

                valid_new_y += direction_y

                if block(new_x, valid_new_y, 0, 0, graph):
                    return None

                if (new_x, valid_new_y) == end:
                    return new_x, valid_new_y
