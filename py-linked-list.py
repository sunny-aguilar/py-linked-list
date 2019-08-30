import node


def main():
    node1 = node.Node(10)
    node2 = node.Node(20)
    node3 = node.Node(30)
    node4 = node.Node(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print('Current Nodes - - - - - - - -')
    show_values(node1)
    add_node(node1, 50)
    add_node(node1, 60)

    print('Current Nodes - - - - - - - -')
    show_values(node1)


def get_val(node):
    print('Node value: ', node.val)


def show_values(node):
    if node is not None:
        temp_node = node

        while temp_node is not None:
            print(temp_node.val)
            temp_node = temp_node.next


def add_node(nodes, val):
    if nodes is not None:
        temp_node = nodes
        while temp_node.next is not None:
            temp_node = temp_node.next

        new_node = node.Node(val)
        temp_node.next = new_node


main()

