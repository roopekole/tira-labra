import unittest
from src.data_structures.heap import Heap


class TestHeap(unittest.TestCase):

    def test_heap_size(self):
        h = Heap()
        self.assertEqual(h.size, -1)
        h.push(1)
        self.assertEqual(h.size, 0)
        h.push(2)
        self.assertEqual(h.size, 1)
        h.pop()
        self.assertEqual(h.size, 0)
        h.pop()
        self.assertEqual(h.size, -1)

    def test_popping_empty_heap(self):
        h = Heap()
        self.assertIsNone(h.pop())

    def test_getting_the_children(self):
        h = Heap()
        h.push(1)
        h.push(2)
        h.push(3)
        self.assertEqual(h.get_children(0, 0, 1), (1, 2))
        self.assertEqual(h.get_children(0, 0, 2), (2, 3))
