import unittest
from src.algorithms.a_star import astar
from src.algorithms.path_find_utilities import euc_dist_heuristic as edh


class TestAStar(unittest.TestCase):

    def test_euc_dist_heuristic(self):
        # Test that Euclidean distance method returns correct distance vertical, horizontal and diagonal

        # Vertical distance down
        self.assertEqual(edh((0, 0), (0, 100)), 100)

        # Vertical distance up
        self.assertEqual(edh((0, 100), (0, 0)), 100)

        # Horizontal distance right
        self.assertEqual(edh((100, 0), (0, 0)), 100)

        # Horizontal distance left
        self.assertEqual(edh((0, 0), (100, 0)), 100)

        # Diagonal distance
        self.assertEqual(round(edh((0, 0), (100, 100)), 2), 141.42)

    def test_a_star_simple_mix_map1(self):
        map = [["@", "@", "@", "@", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", ".", ".", "@"],
               ["@", "@", "@", "@", "@"]]
        start = (1, 1)
        end = (1, 3)
        self.assertEqual(astar(map, start, end, 1)[0], [
                         (1, 1), (2, 1), (3, 2), (2, 3), (1, 3)])

    def test_a_star_simple_mix_map2(self):
        map = [["@", "@", "@", "@", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", "@", ".", "@"],
               [".", "@", ".", ".", "@"],
               ["@", "@", "@", "@", "@"]]
        start = (3, 0)
        end = (1, 3)
        self.assertEqual(astar(map, start, end, 1)[0], [
                         (3, 0), (2, 1), (3, 2), (2, 3), (1, 3)])

    def test_a_star_simple_diagonal(self):
        map = [[".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."]]
        start = (0, 0)
        end = (4, 4)
        self.assertEqual(astar(map, start, end, 1)[0], [
                         (0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])

    def test_a_star_simple_direct_line(self):
        map = [[".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."]]
        start = (3, 0)
        end = (3, 4)
        self.assertEqual(astar(map, start, end, 1)[0], [
                         (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)])

    def test_a_star_no_way_out(self):
        map = [[".", ".", ".", ".", "."],
               [".", "@", "@", "@", "."],
               [".", "@", ".", "@", "."],
               [".", "@", "@", "@", "."],
               [".", ".", ".", ".", "."]]
        start = (2, 2)
        end = (0, 0)
        self.assertIsNone(astar(map, start, end, 1))

    def test_a_star_single_way_out(self):
        map = [[".", ".", ".", ".", "."],
               [".", "@", "@", "@", "."],
               [".", "@", ".", "@", "."],
               [".", "@", "@", ".", "."],
               [".", ".", ".", ".", "."]]
        start = (2, 2)
        end = (0, 0)
        self.assertEqual(astar(map, start, end, 1)[0], [
                         (2, 2), (3, 3), (2, 4), (1, 4), (0, 3), (0, 2), (0, 1), (0, 0)])

    def test_a_star_big_diagonal(self):
        n = 999
        map = [["."] * n] * n
        start = (n, n)
        end = (0, 0)
        self.assertEqual(len(astar(map, start, end, 1)[0]), 1000)
