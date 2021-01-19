# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def maxPathSum(self, root: TreeNode) -> int:
    def maxPathSumH(root):
      if not root:
        return 0, float('-inf')
      leftSum, maxSoFar1 = maxPathSumH(root.left)
      rightSum, maxSoFar2 = maxPathSumH(root.right)
      maxSum = max(root.val, leftSum+root.val, rightSum+root.val)
      maxSoFar = max(maxSoFar1, maxSoFar2, maxSum, leftSum+rightSum+root.val)
      return maxSum, maxSoFar
  
    _, res = maxPathSumH(root)
    return res
  
s = Solution()
root = TreeNode(-3, TreeNode(-1), TreeNode(-2))
print(s.maxPathSum(root))