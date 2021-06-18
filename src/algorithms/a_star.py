import heapq, time
from src.algorithms.path_find_utilities import WALL, MOVEMENTS, reconstruct_path, euc_dist_heuristic


def astar(graph, start, end, dijkstra):

    """

    Args:
        graph: two dimensional list with characters representing walls and floor - remember to adjust the wall constant
        start:
        end:
        dijkstra: Multiplier that effectively turns the A* to Dijkstra by nullifying the euclidean heuristic

    Returns: cheapest path between start and goal found by A* algorithm utilizing euclidean heuristic - none if no path.
            Also return the runtime in milliseconds and iterations (triple)

    """
    current_time = round(time.time() * 1000)
    iterations = 0

    open_set = []
    came_from = {}
    g_score = {start: 0}
    f_score = {start: dijkstra * euc_dist_heuristic(start, end)}
    heapq.heappush(open_set, (f_score[start], start))
    close_set = set()

    while open_set:
        current = heapq.heappop(open_set)[1]

        # Goal found - collect and return the path
        if current == end:
            path = reconstruct_path(start, came_from, current)
            runtime = round(time.time() * 1000) - current_time
            return path, runtime, iterations

        # Add current to the visited node set and check the neighboring nodes
        iterations += 1
        close_set.add(current)
        for i, j in MOVEMENTS:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = g_score[current] + dijkstra * euc_dist_heuristic(current, neighbor)

            # Out of bounds conditions and wall check
            if 0 <= neighbor[0] < len(graph):
                if 0 <= neighbor[1] < len(graph):
                    if graph[neighbor[0]][neighbor[1]] == WALL:
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= g_score.get(neighbor, 0):
                continue

            # Part of the cheapest path. Record the precedence and push the neighbor to queue
            if tentative_g_score < g_score.get(neighbor, 0) or neighbor not in [nb[1] for nb in open_set]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + dijkstra * euc_dist_heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
