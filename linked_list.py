class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def printList(self):
        return '{}'.format(self.data)
    
class Linkedlist:
    def __init__(self):
        self.head = None    

if __name__ == '__main__':

# work of __main__ is to verify that the modules imported for the file are matching
#that of the current file, and hence avoiding copying of code without adding the complete file 
#in the system

    linkList = Linkedlist() #creating object
 
    # assiging values
    phli_node = linkList.head 
    phli_node = Node(2)
    doosri_node = Node(4)
    teesri_node = Node(6)

    # adding pointers
    linkList.next = doosri_node

    doosri_node.next = teesri_node

    teesri_node.next = None

    # traversing nodes
    print(phli_node.printList())
    print(doosri_node.printList())
    print(teesri_node.printList())