


def main():
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(node1.val)


class Node:
    def __init__(self, myval):
        val = myval
        next = None

    def get_val(self):
        return val


def get_val(my_node):
    print('Node value: ', my_node.val)


main()

