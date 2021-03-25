# Singly Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


llist = LinkedList()

first_node = Node("a")
second_node = Node("b")
third_node = Node("c")

llist.head = first_node
first_node.next = second_node
second_node.next = third_node

print(llist)
