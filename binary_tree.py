import random
import plotly_express as px

#The first class is connectored by Binary search tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#The second class is the body of the code
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    #method privated
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
        return(self._search_recursive(self.root, key))
    
    # Method privated
    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)
    
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    #Method privated
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
    
    #Method privated
    def _inorder_traversal_recursive(self, node):
        if node is not None:
            self._inorder_traversal_recursive(node.left)
            print(node.key, end=" ")
            self._inorder_traversal_recursive(node.right)
    
    def preorder_traversal(self):
        self._preorder_traversal_recursive(self.root)
    
    #Method privated
    def _preorder_traversal_recursive(self, node):
        if node is not None:
            print(node.key, end=" ")
            self._preorder_traversal_recursive(node.left)
            self._preorder_traversal_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_traversal_recursive(self.root)
    
    #Method privated
    def _postorder_traversal_recursive(self, node):
        if node is not None:
            self._postorder_traversal_recursive(node.left)
            self._postorder_traversal_recursive(node.right)
            print(node.key, end=" ")

    def duplicate(self, key):
        return self._duplicate_checked(self.root, key)
    
    #Method privated
    def _duplicate_checked(self, node, key):
        if node is None:
            return False
        
        if key == node.key:
            return True
        return self._duplicate_checked(node.right, key)

    def graph(self):
        depths = []
        keys = []
        self._graph_recursive(self.root, 0, depths, keys)
        fig = px.line(x=depths, y=keys, title='Binary Tree Depth vs Key')
        fig.update_layout(
            xaxis_title='Depth',
            yaxis_title='Key'
        )

        fig.show()

    def _graph_recursive(self, node, depth, depths, keys):
        if node is not None:
            self._graph_recursive(node.left, depth + 1, depths, keys)
            depths.append(depth)
            keys.append(node.key)
            self._graph_recursive(node.right, depth + 1, depths, keys)


# Crea una instancia de la clase BST
tree = BST()

# Inserta algunos valores
for i in range(10):
    key = random.randint(1, 100)
    tree.insert(key)

# Verifica que se insertaron correctamente
for i in range(10):
    key = random.randint(1, 100)
    node = tree.search(key)
    if node and node.key == key:
        print(f"{key} is present in the tree")
    else:
        print(f"{key} is NOT present in the tree")

# Verifica que no se inserte un valor duplicado
for i in range(10):
    key = random.randint(1, 100)
    if tree.duplicate(key):
        print(f"{key} is a duplicate value")

# Elimina un valor
tree.delete(50)

# Verifica que se eliminó correctamente
key = 50
node = tree.search(key)
if node is None:
    print(f"{key} was successfully deleted")

# Verifica la ordenación de los valores
print("Inorder traversal:")
tree.inorder_traversal()

# Verifica la ordenación de los valores en preorder y postorder
print("\nPreorder traversal:")
tree.preorder_traversal()

print("\nPostorder traversal:")
tree.postorder_traversal()

    
tree.graph()

