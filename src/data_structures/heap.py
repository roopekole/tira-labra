class Heap:
    """
    Custom min heap implementation of the priority queue. This data structure is used in the project to
    replace python module heapq. Allows for pushing and popping.
    """
    def __init__(self):
        self.heap = []
        self.size = -1

    def push(self, value):
        """

        Args:
            value: Value to be pushed into the queue

        """
        self.size += 1
        if self.size < len(self.heap):
            self.heap[self.size] = value
        else:
            self.heap.append(value)
        self.shift_up(self.size)

    def pop(self):
        """

        Returns: The minimum value in the priority queue

        """
        value = self.heap[0]

        self.heap[0] = self.heap[self.size]
        self.size -= 1
        self.shift_down(0)

        return value

    def shift_up(self, index):
        """
        Shifts up the nodes after pushing the node to queue to restore the min heap
        property

        Args:
            index: node to loop until

        """
        while index > 0:
            parent_index, parent_value = self.get_parent(index)

            if parent_value <= self.heap[index]:
                break

            self.heap[parent_index], self.heap[index] = \
                self.heap[index], self.heap[parent_index]

            index = parent_index

    def shift_down(self, index):
        """
        Shifts down the nodes after pushing the node to queue to restore the min heap
        property
        Args:
            index: node to loop until

        """
        while True:
            index_value = self.heap[index]

            l_leaf_index, l_leaf_value = self.get_children(index, index_value, 1)
            r_leaf_index, r_child_value = self.get_children(index, index_value, 2)

            if index_value <= l_leaf_value and index_value <= r_child_value:
                break

            if l_leaf_value < r_child_value:
                new_index = l_leaf_index
            else:
                new_index = r_leaf_index

            self.heap[new_index], self.heap[index] = self.heap[index], self.heap[new_index]

            index = new_index

    def get_parent(self, index):
        """

        Args:
            index: Given node

        Returns: Parent index and value of the given node in the tree, None if no parent (root)

        """
        if index == 0:
            return None, None

        parent_index = (index - 1) // 2

        return parent_index, self.heap[parent_index]

    def get_children(self, index, default_value, factor):
        """

        Args:
            index: index for which the children are fetched
            default_value:
            factor: 1: left, 2:right

        Returns: index and value of the child node (right of left)

        """
        child_index = 2 * index + factor
        if child_index > self.size:
            return None, default_value

        return child_index, self.heap[child_index]
