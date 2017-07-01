"""
Given a binary tree, find its maximum depth
The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node
"""


# Constructor to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def depth_helper(node):
    # YOUR CODE GOES HERE

    # node with no branches
    if node.left==None and node.right==None:
        return 1
    # node with right branches only
    elif node.left == None:
        return 1+depth_helper(node.right)
    elif node.right == None:
        return 1+depth_helper(node.left)
    else:
        return 1+max(depth_helper(node.left),depth_helper(node.right))

# PLEASE DO NOT CHANGE THIS
def find_max_depth(tree):
    depth = depth_helper(tree)
    return depth


# test cases
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.left.left = Node(8)
    root.left.left.left.left.right = Node(9)
    root.left.left.left.left.right.left = Node(10)
    print("Depth of tree is %d, and the expected result is 7"
          % (find_max_depth(root),))


if __name__ == "__main__":
    main()
