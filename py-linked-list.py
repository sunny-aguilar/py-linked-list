

def main():
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4


class Node:
    def __init__(self, val):
        val = val
        next = None


main()

