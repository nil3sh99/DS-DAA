class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

if __name__ == '__main__':

    linkList = Linkedlist()
    linkList.head = Node(2)
    doosri_node = Node(4)
    teesri_node = Node(6)

    linkList.head.next = doosri_node

    doosri_node.next = teesri_node

    teesri_node.next = None
