
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
    def empty(self):
        self.head = None

    def append(self, node):
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def traverse(self):
        # first check if the linked list is empty
        if not self.head:
            print("Empty linked list")
        temp = self.head
        # linked list is not empty and we have assigned temp to be self.head
        while temp:
            print(temp.data, end=" => " )
            temp = temp.next
            
        print("End")
    
    def insert(self, node, pos):    
        # 0 position will be treated as invalid
        if pos == 0:
            print("invalid address: list indexing not allowed, posistion has to be at least 1")
            return
        elif pos == 1:
            # get the first ever node
            temp = self.head
            # assign temp.next to point to self.head
            temp.next = self.head
            # assign self.head to be temp
            self.head = temp
        else:
            # define a position counter
            p = 0
            # temp node to iterate over
            temp = self.head
            # prev node is needed to keep track of previous node
            prev = temp
            # while we haven't reached the pos we want we keep iterating
            while p < pos - 1 or not temp:
                # re-assign prev to point to current node
                prev = temp
                # re-assign temp to point to next node
                temp = temp.next
                # we haven't yet found our position so increment p by 1
                p +=1
                
            if not temp:
                prev.next = node
            # re-assign prev.next to point to the node we are inserting
            prev.next = node
            # re-assign our new node's next to point to current node
            node.next = temp

    
    
    def deleteNode(self, value):
        if not self.head:
            print("linked list is empty")
            return
        elif self.head.data == value:
            self.head = self.head.next
        else:
            temp = self.head
            prev = temp
            while temp:
                if temp.data == value:
                    prev.next = temp.next
                    break
                else:
                    prev = temp 
                    temp = temp.next

    def findMiddle(self):
        temp = temp1 = self.head
        while temp1 and temp1.next:
            temp = temp.next
            temp1 = temp1.next.next
        print("middle node: ", temp.data)

    def deleteMiddle(self):
        temp = temp1 = self.head
        prev = None
        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp1 = temp1.next.next
        print("middle node : ", temp.data)
        prev.next = temp.next

    def deleteEnds(self):
        self.head = self.head.next
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None

    def sum_of_two_consecutive_nodes(self):
        # as always check if linked list is empty
        if not self.head:
            print("linked list empty")
        # check if self.head is the only element
        elif not self.head.next:
            print("only one element in linked list : ", self.head.data)
        # now we have establised that linked list exists and has two or more elements
        else:
            # define temp to be self.head that is very first node of linked list
            temp = self.head
            # define prev to be temp, we need this to keep track of previous element
            prev = temp
            # while temp exists, iterate over linked list
            while temp:
                # print the sum
                print("sum of two consecutive nodes : ", prev.data + temp.data)
                # re-assign new  prev to be temp
                prev = temp
                # re-assign new temp to be temp.next, that is, the next element in node
                temp = temp.next

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

li = Linked_list()

li.append(Node(1))
li.append(Node(2))
li.append(Node(3))
li.append(Node(4))
li.append(Node(5))
li.append(Node(6))
li.append(Node(7))

li.findMiddle()
li.traverse()
li.deleteEnds()
li.traverse()

# li.reverse()
# li.traverse()