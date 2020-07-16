# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        nums = range(1, n+1)
        return self.generateTreesH(nums)
        
    
    def generateTreesH(self, nums):
        n = len(nums)
        if n == 0:
            return [None]
        elif n == 1:
            return [TreeNode(nums[0])]
        else:
            res = []
            for i in range(n):
                left = self.generateTreesH(nums[0:i])
                right = self.generateTreesH(nums[i+1:])
                for l in range(len(left)):
                    for r in range(len(right)):
                        node = TreeNode(nums[i])
                        node.left = left[l]
                        node.right = right[r]
                        res.append(node)
            return res
            
    def preorderTraversal(self, root):
            sol = []
            stack = []
            stack.append(root)
            
            while (stack):
                cur = stack.pop()
                if cur == None:
                    continue
                sol.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)



            return sol
    
s = Solution()

l = s.generateTrees(0)

# print(l)

for i in range(len(l)):
    # print(l[i])
    print(s.preorderTraversal(l[i]))

        