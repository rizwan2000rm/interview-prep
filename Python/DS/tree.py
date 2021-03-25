# Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value


root = BinaryTree("center-node")
root.left = BinaryTree("left-node")
root.right = BinaryTree("right-node")

print(root)
print(root.left)
print(root.right)

root.left.left = BinaryTree("leftest-node")
root.right.right = BinaryTree("rightest-node")
print(root.left.left)
print(root.right.right)
