import unittest
from src.algorithms.jps import jps, get_full_path, get_direction, get_neighbors, get_successors


class TestJPS(unittest.TestCase):

    def test_jps_simple_mix_map1(self):
        map = [["@", "@", "@", "@", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", ".", ".", "@"],
               ["@", "@", "@", "@", "@"]]
        start = (1, 1)
        end = (1, 3)
        self.assertEqual(jps(map, start, end)[0], [
                         (1, 1), (2, 1), (3, 2), (2, 3), (1, 3)])

    def test_jps_simple_mix_map2(self):
        map = [["@", "@", "@", "@", "@"],
               ["@", ".", "@", ".", "@"],
               ["@", ".", "@", ".", "@"],
               [".", "@", ".", ".", "@"],
               ["@", "@", "@", "@", "@"]]
        start = (3, 0)
        end = (1, 3)
        self.assertEqual(jps(map, start, end)[0], [
                         (3, 0), (2, 1), (3, 2), (2, 3), (1, 3)])

    def test_jps_simple_diagonal(self):
        map = [[".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."]]
        start = (0, 0)
        end = (4, 4)
        self.assertEqual(jps(map, start, end)[0], [
                         (0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])

    def test_jps_simple_direct_line(self):
        map = [[".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."]]
        start = (3, 0)
        end = (3, 4)
        self.assertEqual(jps(map, start, end)[0], [
                         (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)])

    def test_jps_no_way_out(self):
        map = [[".", ".", ".", ".", "."],
               [".", "@", "@", "@", "."],
               [".", "@", ".", "@", "."],
               [".", "@", "@", "@", "."],
               [".", ".", ".", ".", "."]]
        start = (2, 2)
        end = (0, 0)
        self.assertIsNone(jps(map, start, end))

    def test_jps_single_way_out(self):
        map = [[".", ".", ".", ".", "."],
               [".", "@", "@", "@", "."],
               [".", "@", ".", "@", "."],
               [".", "@", "@", ".", "."],
               [".", ".", ".", ".", "."]]
        start = (2, 2)
        end = (0, 0)
        self.assertEqual(jps(map, start, end)[0], [
                         (2, 2), (3, 3), (2, 4), (1, 4), (0, 3), (0, 2), (0, 1), (0, 0)])

    def test_jps_big_diagonal(self):
        n = 1000
        map = [["."] * n] * n
        start = (0, 0)
        end = (n-1, n-1)
        self.assertEqual(len(jps(map, start, end)[0]), 1000)

    def test_full_path_diagonal(self):
        path = [(0, 0), (5, 5)]
        self.assertEqual(get_full_path(path), [
                         (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    def test_full_path_vertical(self):
        path = [(0, 0), (5, 0)]
        self.assertEqual(get_full_path(path), [
                         (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])

    def test_full_path_horizontal(self):
        path = [(0, 0), (0, 5)]
        self.assertEqual(get_full_path(path), [
                         (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)])

    def test_all_directions(self):
        path = []
        start = (0, 0)
        path.append(start)
        jp1 = (3, 3)  # move diagonally to point (3,3)
        path.append(jp1)
        jp2 = (0, 6)  # move diagonally to point (0,6)
        path.append(jp2)
        jp3 = (6, 6)  # move vertically to point (6,6)
        path.append(jp3)
        end = (6, 0)  # move horizontally to point (6,0)
        path.append(end)
        self.assertEqual(len(get_full_path(path)), 19)
        self.assertEqual(get_full_path(path), [(0, 0), (1, 1), (2, 2), (3, 3), (2, 4), (1, 5), (0, 6),
                                               (1, 6), (2, 6), (3, 6), (4,
                                                                        6), (5, 6), (6, 6),
                                               (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)])
