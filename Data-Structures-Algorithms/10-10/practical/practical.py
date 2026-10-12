
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
            print("node : ", temp.data)
            temp = temp.next
            
        print("traversal complete")
    
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
    def findMiddle(self):
        # declare variables needed throughout method's lift
        length = 0
        temp = self.head
        p = 0

        # iterating over linked list to get it's total length
        while temp:
            temp = temp.next
            # increment length while temp exists
            length +=1

        # do a simple floor division to get the lower bound of the middle in case it's odd we will take the previous element and same in case of even
        middle =  length // 2
        temp = self.head
        while p <= middle:
            if p == middle:
                print("middle node : ", temp.data)
                break
            else:
                temp = temp.next
                p += 1
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

    def reverseList(self):
        # check if linked list is empty
        if not self.head:
            print("Linked list is empty")
            return
        # linked list is not empty here
        else:       
            # define a list to store every element of linked list  
            arr = []
            # define temp to be self.head
            temp = self.head
            # while temp exists, we wil iterate over linked list
            while temp:
                #  we will append node to arr list
                arr.append(temp.data)
                #  re-assign temp to be temp.next, that is, the next node
                temp = temp.next
            # empty the linked list before adding to it so we don't add all the element after the original list
            self.empty()
            # iterate over arr list in reverse order
            for i in range(len(arr) - 1, -1, -1):
                #  append node to it
                self.append(Node(arr[i]))
       
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


li = Linked_list()
li.append(Node(1))
li.append(Node(2))
li.append(Node(3))
li.append(Node(4))
li.append(Node(5))

li.traverse()
