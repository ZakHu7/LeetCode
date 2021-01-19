# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    small = min(p.val, q.val)
    big = max(p.val, q.val)
    while root:
      if small <= root.val and big >= root.val:
        return root
      if big < root.val:
        root = root.left
      elif small > root.val:
        root = root.right
    return None