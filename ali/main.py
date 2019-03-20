class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def func(node1, node2):
    if node1 is None:
        return node2
    elif node2 is None:
        return node1

    origin = Node(213231342, None)
    current = origin

    while node1 is not None and node2 is not None:
        if node1.val <= node2.val:
            current.next = node1
            node1 = node1.next
        else:
            current.next = node2
            node2 = node2.next
        current = current.next
    if node2 is None:
        current.next = node1
    elif node1 is None:
        current.next = node2
    return origin.next


node1_3 = Node(7, None)
node1_2 = Node(5, node1_3)
node1_1 = Node(3, node1_2)

node2_3 = Node(6, None)
node2_2 = Node(4, node2_3)
node2_1 = Node(2, node2_2)

result_node = func(node1_1, node2_1)

while result_node is not None:
    print(result_node.val)
    result_node = result_node.next
