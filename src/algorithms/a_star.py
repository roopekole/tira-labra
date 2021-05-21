import math
from queue import PriorityQueue


class Node:
    def __init__(self, value, parent, start, end):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.end = end

    def get_pos(self):
        return self.row, self.col

    def visited(self):
        return

def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


