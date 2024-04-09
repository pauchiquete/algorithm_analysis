import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedlistN:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def delete(self, data):
        if not self.head:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return 
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True 
            current = current.next
        return False
    
    def traverse(self):
        elements =[]
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def numpy_array(self):
        return np.array(self.traverse())
    
    
    def graph(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        
        plt.figure(figsize = (10, 5))
        plt.subplot(121)
        plt.bar(range(len(nodes)), nodes)
        plt.title('Linked list')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.subplot(122)
        plt.plot(np.array(nodes))
        plt.title('Array view')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.show()



# Crear una lista enlazada
ll = LinkedlistN()

# Insertar algunos elementos
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.insert(20)

# Mostrar los elementos de la lista enlazada
print("Elementos de la lista enlazada:", ll.traverse())

# Convertir la lista enlazada a un arreglo NumPy
numpy_array = ll.numpy_array()
print("Arreglo NumPy:", numpy_array)

# Eliminar un elemento de la lista enlazada
ll.delete(10)
print("Elementos de la lista enlazada después de eliminar 10:", ll.traverse())

# Buscar un elemento en la lista enlazada
print("¿El número 15 está en la lista?", ll.search(15))
print("¿El número 25 está en la lista?", ll.search(25))



ll.graph()
