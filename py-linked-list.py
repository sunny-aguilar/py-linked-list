
import node


def main():
    node1 = node.Node(10)
    node2 = node.Node(20)
    node3 = node.Node(30)
    node4 = node.Node(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4


def getVal(node):
    print('Node value: ')


main()

