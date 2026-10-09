# Linked List 

# how to insert a node at any position
# time complexity for inserting to a singly linked-list is O(1)

# we take newnode.next and point to the next node's address

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:

    def __init__(self):
        self.head = None

    def push(self, node):
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def insert(self, node, pos):
        # this block executes if you want to insert at first position, that is, at head position
        if pos == 1 or pos == 0:
            # this block executes if linked list is empty, that is, self.head is None
            if not self.head:
                #  simply sets self.head to be node
                self.head = node
            # this block executes if linked list is not empty
            else:
                node.next = self.head 
                self.head = node

        # this block executes for every other pos value
        else:
            p = 1
            temp = self.head
            while p != pos - 1:
                # this block executes if linked list exhausts before pos is reached
                if not temp.next:
                    # breaks if linked list ends
                    break
                #  for regular inserts
                temp = temp.next
                p+=1

            # add node to position
            node.next = temp.next
            temp.next = node

    def deleteByPosition(self, pos):
        if pos == 0:
            print("invalid position")
            return
        if pos == 1:
            if not self.head:
                print("list already empty")
            else:
                temp = self.head
                self.head = temp.next
        else:
            temp = self.head
            prev = temp
            p = 1
            while p < pos:
                prev = temp
                temp= temp.next
                p+=1
            prev.next = temp.next
            temp = None


    def delete(self, value):
        temp = self.head
        if temp.data == value:
            self.head = self.head.next
        else:
            prev = None
            while temp.data != value:
                prev = temp
                temp = temp.next
            
            if not temp:
                print("value is not present")
                return
            prev.next = temp.next
            temp = None
           
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

li = linked_list()
li.push(node(0))
li.push(node(1))
li.push(node(2))
li.push(node(3))
li.push(node(4))

li.print()

print("--------------------------------------------")
li.insert(node(12), 0)
li.print()
li.deleteByPosition(1)
li.deleteByPosition(3)
li.deleteByPosition(0)
print("--------------------------------------------")
li.print()