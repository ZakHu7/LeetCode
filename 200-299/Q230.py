# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
from collections import deque
class Solution:
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    stack = deque()
    while root or stack:
      while root.left:
        stack.append(root)
        root = root.left
      root = stack.pop()
      k -= 1
      if k == 0:
        return root.val
      root = root.right
    return -1