import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

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
