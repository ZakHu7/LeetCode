# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # does not have to sort it
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """

        if root == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        
        tail = root.left
        while tail != None and tail.right != None:
            tail = tail.right

        if root.left != None:
            tail.right = root.right
            root.right = root.left
            root.left = None
        


                
s = Solution()

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)


b.right = d
b.left = c
a.left = b
a.right = e
e.right = f

s.flatten(a)

print(a)