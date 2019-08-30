# node class


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def get_val(self):
        return self.val

