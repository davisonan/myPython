#' % Tree-based data structures
#' % Xu Tian
#' % 2017/03/28


#' # Background
#' This writeup is motivated by tree-based problems in leetcode and is expanded
#' to embrace as complete a set of knoweldge as possible. Like linked lists,
#' trees are made up of nodes. A common kind of tree is a binary tree. The most
#' commonly used and tested method is called binary search tree and we'll start
#' from it. Trees are recursive data structures because they are defined
#' recursively.

#' # Binary search tree
#' The binary search tree is


class Node(object):
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
    def __str__(self):
        return "Node with value {}.".format(self.val)

a = Node(2)
b = Node(3)
c = Node(4)
d = Node(5, b, c)
e = Node(6, Node(7), Node(8))


class BST(object):
    def __init__(self, val=0):
        self.root = Node(val)
        self.maxDepth = 0
        self.nNodes = 0
    def __len__(self):
        return self.nNodes

    def __iter__(self):
        """Define the iterator for the binary search tree."""
        pass

    def add(self, newNode):
        pass

    def getMaxDepth(self):
        if root is None: return 0
        return 1 + max(self.getMaxDepth(self.root.left),
                       self.getMaxDepth(self.root.right))

    def total(self):
        def f1(node):
            if node == None: return 0
            return f1(node.left) + f1(node.right) + node.val
        return f1(self.root)

    def __str__(self):
        def f2(root):
            if root:
                print(root.val)
                f2(root.left)
                f2(root.right)
        f2(self.root)

    def printPostOrder(self):
        def f3(root):
            if root:
                f3(root.left)
                f3(root.right)
                print(root.val)
        f3(self.root)

    def printInOrder(self):
        def f4(root):
            if root:
                f4(root.left)
                print(root.val)
                f4(root.right)
        f4(self.root)

    def printInOrderGraphical(self):
        def f5(root, lvl=0):
            if root:
                f5(root.left, lvl+1)
                print(' ' * lvl + str(root.val))
                f5(root.right, lvl+1)
        f5(self.root)

    def invert(self):
        """Invert the tree."""
        pass

    def calDiameter(self):
        """Calculate the diamter of the tree defined as the longest path between
        any two nodes in the tree."""

bst1 = BST(6)

class Solution(object):
    def sortedArrayToBST(self, nums):
        n = len(nums)
        if n == 0: return None
        mid = n//2
        root = Node(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = sol.sortedArrayToBST(nums)


def printBST(root):
    if root is None: return
    print(root.val)
    printBST(root.left)
    printBST(root.right)

printBST(root)
