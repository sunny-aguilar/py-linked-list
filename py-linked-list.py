import node


def main():
    node1 = node.Node(10)
    node2 = node.Node(20)
    node3 = node.Node(30)
    node4 = node.Node(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    show_values(node1)


def get_val(node):
    print('Node value: ', node.val)


def show_values(node):
    if node is not None:
        tempNode = node

        while tempNode is not None:
            print(tempNode.val)
            tempNode = tempNode.next




main()

