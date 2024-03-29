import nodes


def main():
    node1 = nodes.Node(10)

    print('\nCurrent Nodes - - - - - - - -')
    show_values(node1)
    add_node(node1, 20)
    add_node(node1, 30)

    print('\nCurrent Nodes - - - - - - - -')
    show_values(node1)

    # add a front node
    add_node_front(node1, 5)

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
    else:
        print('List is empty.')


def add_node(node, val):
    if node is not None:
        temp_node = node
        while temp_node.next is not None:
            temp_node = temp_node.next

        new_node = nodes.Node(val)
        temp_node.next = new_node
        new_node.prev = temp_node
    else:
        print('Adding a node to the empty list.')
        temp_node = nodes.Node(val)
        temp_node.next = None


def add_node_front(node, val):
    if node is not None:
        new_node = nodes.Node(val)
        new_node.next = node
    else:
        new_node = nodes.Node(val)
        new_node.next = None


def get_front_node(node):
    if node is not None:
        print(node.val)
    else:
        print('List is empty.')


def get_back_node(node):
    temp_node = node
    if node is not None:
        while temp_node.next is not None:
            temp_node = temp_node.next
            print(temp_node.val)
    else:
        print('List is empty.')


def delete_node(node):
    temp_node = node
    temp_node_next = node.next
    if node is not None:
        while temp_node is not None:
            temp_node_next = temp_node.next
            del temp_node
    else:
        print('List is empty.')

# get back node
# delete node

main()

