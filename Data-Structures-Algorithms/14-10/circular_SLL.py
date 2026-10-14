# singly circular linked list


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
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
        node.next = self.head

    def traverse(self):
        # first check if the linked list is empty
        if not self.head:
            print("Empty linked list")
        temp = self.head
        # linked list is not empty and we have assigned temp to be self.head
        while temp.next != self.head:
            print(temp.data, end=" => " )
            temp = temp.next
            
        print("End")

    
    def insert(self, node, pos):
        # this block executes if you want to insert at first position, that is, at head position
        if pos == 1 or pos == 0:
            # this block executes if linked list is empty, that is, self.head is None
            if not self.head:
                #  simply sets self.head to be node
                self.head = node
                
            # this block executes if linked list is not empty
            else:
                # get first node
                t = self.head
                #  iterate until we find last node
                while t.next != self.head:
                    t = t.next

                # update last node's next to point to new node
                t.next = node
                #  update node.next to point self.head
                node.next = self.head 

                # update self.head to be new node
                self.head = node

        # this block executes for every other pos value
        else:
            p = 1
            temp = self.head
            while p != pos - 1 and temp.next != self.head:
                # this block executes if linked list exhausts before pos is reached

                # for regular inserts
                temp = temp.next

                p+=1

            # add node to position
            node.next = temp.next
            temp.next = node

    def delete(self,value):
        temp=self.head
        pre=None
        if temp is None:
            print("List is empty")
            return
        if temp.data==value:
            self.head=self.head.next
            while temp.next!=self.head: # find the last node
                temp=temp.next 
            temp.next=self.head
        else:
            while temp and temp.data!=value:
                pre=temp
                temp=temp.next
            if temp==self.head:
                print("value is not present ")
                return
            pre.next=temp.next
            temp=None
    

li = Linked_list()
li.append(Node(1))
li.append(Node(2))
li.append(Node(3))
li.append(Node(4))
li.append(Node(5))
li.append(Node(6))
li.insert(Node(1000), 12)
li.traverse()