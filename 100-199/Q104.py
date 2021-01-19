# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
from collections import deque
class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    if not root: 
      return 0
    count = 0
    queue = deque()
    queue.append(root)
    while queue:
      level = len(queue)
      count += 1
      for i in range(level):
        cur = queue.popleft()
        if cur.left:
          queue.append(cur.left)
        if cur.right:
          queue.append(cur.right)
    return count
      
    