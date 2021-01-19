# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
from typing import List
from collections import deque
class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
      return []
    queue = deque([root])
    res = []
    while queue:
      length = len(queue)
      curLevel = []
      for _ in range(length):
        cur = queue.popleft()
        curLevel.append(cur.val)
        if cur.left:
          queue.append(cur.left)
        if cur.right:
          queue.append(cur.right)
      res.append(curLevel)
    return res
    