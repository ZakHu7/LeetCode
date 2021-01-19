# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
from collections import deque
class Solution:
  def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    def isSubtreeH(s, preOrder):
      if not s:
        preOrder.append('#')
      else:
        preOrder.append(str(s.val))
        isSubtreeH(s.left, preOrder)
        isSubtreeH(s.right, preOrder)
    
    spreOrder = []
    tpreOrder = []
    isSubtreeH(s, spreOrder)
    isSubtreeH(t, tpreOrder)
    return ''.join(tpreOrder) in ''.join(spreOrder)
      
# from collections import deque
# class Solution:
#   def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#     def isSubtreeH(s, cur):
#       if s and cur:
#         if s.val != cur.val:
#           return False
#         return isSubtreeH(s.left, cur.left) and isSubtreeH(s.right, cur.right)
#       return s is cur
    
#     stack = deque([s])
#     while stack:
#       root = stack.pop()
#       if isSubtreeH(root, t):
#         return True
#       if root.left:
#         stack.append(root.left)
#       if root.right:
#         stack.append(root.right)
      
#     return False
      