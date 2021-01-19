# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
from typing import List
from collections import deque
class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack = deque()
    res = []
    while root or stack:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      res.append(root.val)
      root = root.right
    return res
  
  
s = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))

print(s.inorderTraversal(root))