
import matplotlib.pyplot as plt

#THe first class represents a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#The second class represents entire linked list and contains the "head" of code
class Linkedlist:
    def __init__(self):
        self.head = None

    def create_node(self, data):
        new_node = Node(data)
        return new_node
    
    def connect_node(self, node1, node2):
        node1.next = node2

    def add_node(self, data):
        new_node = self.create_node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_node(self, data, position):
        new_node = self.create_node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(position-1):
            if not current:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, data):
        if not self.head:
            raise ValueError("List is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError("Value not found in the list")
    
    def graph(self):
        nodes = []
        current = self.head
        i = 0
        while current:
            nodes.append((i, current.data))
            current = current.next
            i += 1

        x = [node[0] for node in nodes]
        y = [node[1] for node in nodes]

        plt.plot(x, y)
        plt.xlabel("Node Index")
        plt.ylabel("Node Value")
        plt.title("Linked List Graph")

        plt.show()

    

ll = Linkedlist()

ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

print('Linked list: ')
current = ll.head
while current:
    print(current.data)
    current = current.next

ll.insert_node(0, 0)
ll.insert_node(4, 4)

print('Linked list after inserting datas')
current = ll.head
while current:
    print(current.data)
    current = current.next

ll.delete_node(0)
ll.delete_node(4)

print('Linked list after deleting datas')
current = ll.head
while current:
    print(current.data)
    current = current.next



ll.graph()   

    
