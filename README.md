# Algorithm_analysis


## An implementation for linked lists is built.

A linked list is a linear data structure similar to arrays. It consists of nodes, where each node contains two elements: the data and a reference to the next node. The first node is called the head and is used as the starting point for any iteration through the list. The last node should have its reference to the next node pointing to None to determine the end of the list.

Linked lists serve a variety of purposes in the real world. They can be used to implement queues or stacks, as well as graphs. They are also useful for much more complex tasks, such as managing the lifecycle of an operating system application.


## Steps for a linked list just using python libraries

First, we create two classes. The first one will have the Node that will do the function of connecting to the list and the second one will be our body code, it will contain all the other requirements we need to make the linked list.

- We create the class that we will call Node and also the variable data where our data will be. The other variable that we call next, we do not define it in the class as such since it will serve us to make the function of jumps between our nodes reason why it does not need a value, it will only be null.

~~~python
import matplotlib.pyplot as plt

#THe first class represents a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
~~~

- As I mentioned at the beginning, we create another class that will contain the body of the cross-list, so here we define our functions that we are going to implement. Nothing is defined in the init because we are going to use the data that we defined in the previous class. We only add a variable called head that will be the "head" of our code and as with the next variable, they are null.

~~~python
#The second class represents entire linked list and contains the "head" of code
class Linkedlist:
    def __init__(self):
        self.head = None
~~~

In general, each function that was implemented is necessary for our code to work efficiently. As we can see we defined 6 functions if we count the graph. Each function gives us a different result that I will explain below:

- In the first function "create_node" only one node is created from our Node class.
- In the second function "connect_node" adds the nodes so that they are connected to each other, since we need at least two nodes to generate a linked list.

- In the third function "add_node" adds the nodes obtained to the "head" of our code as long as they have not been defined within it, they can be added at the same time that they will be passing to the next report as more data is added.

- In the fourth function "insert_node" will be added according to the positions that we put the user, if these become less than -1 will get an error message in the index.

- In the fifth function "delete_node" we delete the data of our nodes. Here we mainly condition, for example if it is out of our "head" it sends an error message. Also if the value you want to delete is not in the cross list you will get a message that the data was not found.

- Finally, in the sixth function "graph" we generate a graph to see the behavior of our code.

~~~python
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
~~~

I test my code.
~~~python
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

~~~
These were my results.
![Resultado](img\result.PNG)
![Resultado](img\graph2.PNG)

## Steps a linked list using Numoy library
To test the performance of our code, another linked list was made using the numpy library. Which to some extent is different from our previous code. In this code are still almost the same functions that we used before only we added a new function called "numpy_array" which converts our linked list to an array. This is because the numpy library handles array data so there is no linked list in the numpy library.

~~~python
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
    #This function makes the path of our linked list 
    def traverse(self):
        elements =[]
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    #This function converts our linked list to an array
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

~~~

I test my code 
~~~python
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
~~~

There were my results.
![Resultado](img\numpy.PNG)
![Resultado](img\graph.PNG)

# Binary Search Tree
A binary search tree (BST) is a data structure that allows efficient insertion, deletion, and searching of elements. Each node in a BST has a maximum of two children. For each node, the values of its left descendant nodes are less than the current node, which in turn is less than the right descendant nodes. This structure allows each search, insertion, or deletion to take time proportional to the logarithm of the number of items stored in the tree, that is, O(log n).

BSTs are commonly used to implement efficient search operations, insertions, and deletions. Some specific uses include:

- Maintaining data in sorted order.

- Implementing symbol tables, which are used to store data such as variable and function names in a programming language.

- In some cases, they can be used as graphs to represent a collection of information.

- They are used in many 3D video games to determine which objects need to be rendered.

- They are used in almost all high-bandwidth routers to store routing tables.

## Steps a binary search tree
As with our linked list, we need two classes to generate our binary search tree. The first one is where our node that connects our data in the form of a tree will be and the second one is the body of our tree where all the functions that we are going to use are stored.

- We create our first class "Node" in which we define only our input value which is the key. As null values we define right and left. These will help us to position our values which can be higher (right) or lower (left).

~~~python
#The first class is connectored by Binary search tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
~~~

- It was mentioned at the beginning that we need two classes. For our second class we will inherit the data we defined in our first class. Also this is where the body of our code will be. In the init nothing is defined as such, only the root, which is the root of our tree.

~~~python
#The second class is the body of the code
class BST:
    def __init__(self):
        self.root = None
~~~

In general, each defined function of our code helps to realize our binary tree. However, we must take into account that for this code we defined private methods, which are very common when making binary search trees, so these are not shown to the user and is where the execution of the steps is contained, to use them we used public methods, in which we only call the private function and there the code is executed. This was done mainly to avoid problems of optimization and modification by the user. Now, let's explain each implemendata function in our code:

- In the "first" function "insert" we only call its recursive function to execute this function. Now, in the function "insert_recursive" we will add our data, taking into account that if the key is smaller than the node.key this will be positioned on the left and if it is bigger it will be on the right.

- In the "second" function "search" is called only to its recursive function "search_binary" which will execute the search function of the value that we are looking for, if it finds it then it will return the value of that node, if that value is bigger than our node.key it will look for it in the values that are to the right and if it is smaller in the left.

- In the "third" function "delete" we only call its recursive function "delete_recursive" is the one that will execute the function of deleting the nodes and their values, this will depend on the position in which the node is found, that is to say if it is on the right or left.

- In the fourth function "find_min_value" it will only look for the minimum value of our tree and this will generally be on the left.

- In the "fifth", "sixth", and "seventh" functions "inorder_traversal", "preorder_traversal" and "postorder_traversal" only call their recursive function "inorder_traversal_recursive", "preorder_traversal_recursive" and "postorder_traversal_recursive" which will show the in order, pre order and post order of the data that are in our nodes.

- In the "eighth" function "duplicate" we will only call its recursive function "duplicated_checked" in which it will search if there are repeated values in the tree, since one of the conditions of the binary search trees is that there are not equal values.

- Finally, the ninth function will display a graph to visualize the performance of our code.

~~~python
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.key = self._find_min_value(node.right)
            node.right = self._delete_recursive(node.right, node.key)
        return node

    def _find_min_value(self, node):
        min_value = node.key
        while node.left is not None:
            min_value = node.left.key
            node = node.left
        return min_value

    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        if node is not None:
            self._inorder_traversal_recursive(node.left)
            print(node.key, end=" ")
            self._inorder_traversal_recursive(node.right)

    def preorder_traversal(self):
        self._preorder_traversal_recursive(self.root)

    def _preorder_traversal_recursive(self, node):
        if node is not None:
            print(node.key, end=" ")
            self._preorder_traversal_recursive(node.left)
            self._preorder_traversal_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_traversal_recursive(self.root)

    def _postorder_traversal_recursive(self, node):
        if node is not None:
            self._postorder_traversal_recursive(node.left)
            self._postorder_traversal_recursive(node.right)
            print(node.key, end=" ")

    def duplicate(self, key):
        return self._duplicate_checked(self.root, key)

    def _duplicate_checked(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        return self._duplicate_checked(node.right, key)

    # Función para generar las posiciones de los nodos
    def generate_positions(self, root, pos, x=0, y=0, width=1000, height=1000, depth=0):
        if root is None:
            return
        self.generate_positions(root.left, pos, x - width / 2 ** (depth + 1), y - height, width / 2, height, depth + 1)
        pos[root.key] = (x, y)
        self.generate_positions(root.right, pos, x + width / 2 ** (depth + 1), y - height, width / 2, height, depth + 1)

    # Función para generar la gráfica del árbol
    def draw_tree(self):
        pos = {}
        self.generate_positions(self.root, pos)
        G = nx.Graph()
        self.draw_edges(self.root, pos, G)
        nx.draw(G, pos=pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_weight='bold')
        plt.title("Binary Search Tree")
        plt.show()

    # Función para dibujar las aristas del árbol
    def draw_edges(self, root, pos, G):
        if root is None:
            return
        if root.left:
            G.add_edge(root.key, root.left.key)
            self.draw_edges(root.left, pos, G)
        if root.right:
            G.add_edge(root.key, root.right.key)
            self.draw_edges(root.right, pos, G)

~~~

I test my code 
~~~python

if __name__ == "__main__":
    # Creamos un árbol de prueba
    bst = BST()
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)

    # Ejecutamos los diferentes tipos de recorridos en el árbol
    print("Inorder Traversal:")
    bst.inorder_traversal()

    print("Preorder Traversal:")
    bst.preorder_traversal()

    print("Postorder Traversal:")
    bst.postorder_traversal()

    # Graficamos el árbol
    bst.draw_tree()

~~~

Show the results 
![Resultado](img\tree.PNG)
![Resultado](img\graph4.PNG)