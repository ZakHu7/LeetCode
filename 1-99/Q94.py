# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        sol = []
        stack = []
        cur = root
        
        while True:
            # print(stack)
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif (stack):
                cur = stack.pop()
                sol.append(cur.val)
                cur = cur.right
            else:
                break

        return sol


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.right = b
b.left = c

s = Solution()
r = s.inorderTraversal(a)

# print(a.val)
print(r)