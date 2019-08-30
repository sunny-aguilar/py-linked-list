import nodes


def main():
    node1 = nodes.Node(10)
    node2 = nodes.Node(20)
    node3 = nodes.Node(30)
    node4 = nodes.Node(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print('\nCurrent Nodes - - - - - - - -')
    show_values(node1)
    add_node(node1, 50)
    add_node(node1, 60)

    print('\nCurrent Nodes - - - - - - - -')
    show_values(node1)


def get_val(node):
    print('Node value: ', node.val)


def show_values(node):
    if node is not None:
        temp_node = node

        while temp_node is not None:
            print(temp_node.val)
            temp_node = temp_node.next


def add_node(node, val):
    if node is not None:
        temp_node = node
        while temp_node.next is not None:
            temp_node = temp_node.next

        new_node = nodes.Node(val)
        temp_node.next = new_node


def add_node_front(node, val):
    if node is not None:
        new_node = nodes.Node(val)
        new_node.next = node



main()

