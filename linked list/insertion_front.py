class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None    
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data),
            temp = temp.next
    def push(self, new_data):
        new_node = Node(new_data)

        # make next of new node as head
        new_node.next = self.head
        # move the head to point to new node
        self.head = new_node

if __name__ == '__main__':

# work of __main__ is to verify that the modules imported for the file are matching
#that of the current file, and hence avoiding copying of code without adding the complete file 
#in the system

    linkList = Linkedlist() #creating object
 
    # assiging values
    linkList.head = Node(2)
    doosri_node = Node(4)
    teesri_node = Node(6)

    # adding pointers
    linkList.head.next = doosri_node

    doosri_node.next = teesri_node

    teesri_node.next = None
    # traversing nodes
    linkList.printList()
    # pushing new node
    linkList.push(0)