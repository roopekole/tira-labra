from collections import OrderedDict
PATH, WALL = ".", "@"


def find_neighbors(coords, nested_list):
    row, col = coords

    visited = (
        discover_room((row - 1, col), nested_list),  # North
        discover_room((row + 1, col), nested_list),  # South
        discover_room((row, col + 1), nested_list),  # East
        discover_room((row, col - 1), nested_list),  # West
        discover_room((row - 1, col + 1), nested_list),  # Northeast
        discover_room((row + 1, col + 1), nested_list),  # Southeast
        discover_room((row + 1, col - 1), nested_list),  # Southwest
        discover_room((row - 1, col - 1), nested_list),  # Northwest
    )
    return [v for v in visited if isinstance(v, tuple)]


def discover_room(coords, nested_list):
    width, height = len(nested_list[0]), len(nested_list)
    row, col = coords

    if any((row < 0, row > height - 1, col < 0, col > width - 1)):
        return False
    elif nested_list[row][col] == PATH:
        return row, col
    else:
        return False


def nested_list2adjlist(nested_list):
    adjlist = OrderedDict()

    for row_idx, row in enumerate(nested_list):
        for col_idx, c in enumerate(row):
            coords = (row_idx, col_idx)
            if discover_room(coords, nested_list):
                new_room = Room(coords, find_neighbors(coords, nested_list))
                adjlist.update({coords: new_room})
    return adjlist


class Room:
    def __init__(self, coords, neighbors=None, traversal_mode=False):
        self.coords = coords
        if neighbors:
            self.neighbors = neighbors
        else:
            self.neighbors = []

        # Derived Attributes
        self.row, self.col = self.coords
        self.is_intersection = len(self.neighbors) > 2
        self.is_dead_end = len(self.neighbors) == 1

        # These don't come into play until the traversal stage
        self.prev = None
        self.traversal_mode = traversal_mode

    def __repr__(self):
        if self.traversal_mode and self.prev:
            return f"""{self.prev} -> {self.coords}"""
        elif self.traversal_mode and not self.prev:
            return f"""{self.coords}"""
        else:
            return f"""Neighbors={self.neighbors}, Intersection={self.is_intersection}, Dead End={self.is_dead_end}"""