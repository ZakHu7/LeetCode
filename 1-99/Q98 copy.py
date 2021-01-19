# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def isValidBST(self, root: TreeNode) -> bool:
    def isValidBSTH(node, leftBound, rightBound):
      if not node:
        return True
      return (leftBound < node.val < rightBound
              and isValidBSTH(node.left, leftBound, node.val)
              and isValidBSTH(node.right, node.val, rightBound))
      
      
    return isValidBSTH(root, float('-inf'), float('inf'))