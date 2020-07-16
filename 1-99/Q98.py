# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        return self.isValidBSTH(root, float('-inf'), float('inf'))
    def isValidBSTH(self, root, small, big):
        if root == None:
            return True
        else:
            val = root.val
            if val > small and val < big:
                return self.isValidBSTH(root.left, small, val) and self.isValidBSTH(root.right, val, big)
            else:
                return False

s = Solution()

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)


a.right = c
c.right = b
c.left = d

print(s.isValidBST(a))
        