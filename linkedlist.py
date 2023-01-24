#create a node
class node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next


#create a class for the linked list
class linked_list:
    def __init__(self):
        self.head = None
    #function to add a node at the front of the list
    def add_front(self, data):
        self.head = node(data=data, next=self.head)  
    #add node at end
    def add_end(self, data):
        if not self.head:
            self.head = node(data = data)
            return
        curr = self.head
        while curr.next :
            curr = curr.next
        curr.next = node(data = data)
    #delete any node
    def get_last_node(self):
        temp = self.head
        while (temp.next is not None):
            temp = temp.data
    #print list nodes
    def prin_list(self):
        node = self.head
        while node != None:
            print(node.data, end = "^^")
            node = node.next
            
#calling all functions
ll = linked_list()
ll.add_front(17)
ll.add_end(6)
ll.add_front(7)
ll.prin_list()     