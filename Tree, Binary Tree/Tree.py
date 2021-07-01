class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def predorder(self, v):
        if v:
        #M-L-R
            print(v.key, end=' - ')
            self.predorder(v.left)
            self.predorder(v.right)

    def inorder(self, v):
        # L-M-R
        if v:
            self.inorder(v.left)
            print(v.key, end=' - ')
            self.inorder(v.right)

    def postorder(self, v):
        # L-R-M
        if v:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' - ')

T = Tree()
a, b, c, d = Node(1), Node(2), Node(3), Node(4)
T.root = a
a.left = b
a.right = c
b.parent = c.parent = a
c.left = d
d.parent = b
T.predorder(T.root)
print()
T.inorder(T.root)
print()
T.postorder(T.root)