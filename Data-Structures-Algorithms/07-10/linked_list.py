# Linked list file

# Singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    base = None
    end = None
    def __init__(self):
        self.base = None

    def push(self, new_node : Node):
        if self.base== None:
            self.base = new_node
        else:
            temp = self.base
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print(self):
        temp = self.base
        while temp:
            print(temp.data)
            temp = temp.next

n1 = Node(0)
n2 = Node(12)
n3 = Node(90)

list1 = Linked_list()
list1.push(n1)
list1.push(n2)
list1.push(n3)

list1.print()