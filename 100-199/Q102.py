# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):

        if root == None:
            return []

        res = []    
        thisLevel = []
        thisLevel.append(root)

        while (thisLevel):
            row = []
            nextLevel = []

            for node in thisLevel:
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)
                row.append(node.val)
                
            thisLevel = nextLevel
            
            res.append(row)
        
        return res

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

print(s.levelOrder(a))