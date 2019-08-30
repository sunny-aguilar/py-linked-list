# node class


class Node:
    def __init__(self, myval):
        self.val = myval
        self.next = None
        self.prev = None

    def get_val(self):
        return self.val

