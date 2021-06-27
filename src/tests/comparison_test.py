import unittest
from src.algorithms.jps import jps
from src.algorithms.a_star import astar


class TestComparison(unittest.TestCase):

    # This test class will cross validate the functioning of the algorithms.

    def test_cross_test_1(self):
        map = [["@", "@", "@", "@", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", ".", ".", "@"],
               ["@", ".", ".", "@", "@"],
               ["@", ".", ".", ".", "@"],
               ["@", ".", "@", "@", "@"],
               ["@", "@", "@", ".", "@"],
               ["@", "@", "@", "@", "@"]]
        start = (1, 1)
        end = (1, 3)
        self.assertEqual(jps(map, start, end)[0], astar(map, start, end, 1)[0])
        self.assertEqual(jps(map, start, end)[0], astar(map, start, end, 0)[0])
        start = (1, 3)
        end = (1, 1)
        self.assertEqual(jps(map, start, end)[0], astar(map, start, end, 1)[0])
        self.assertEqual(jps(map, start, end)[0], astar(map, start, end, 0)[0])
