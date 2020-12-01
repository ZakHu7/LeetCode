# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
          return []
        h = self.getTreeHeight(root)
        res = [[] for _ in range(h+1)]
        level = 0
        queue = deque()
        queue.append(root)

        while queue:
          length = len(queue)
          for _ in range(length):
            node = queue.popleft()
            res[h-level].append(node.val)
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
          level += 1
        return res
    def getTreeHeight(self, root):
      if not root:
        return -1
      return 1 + max(self.getTreeHeight(root.left), self.getTreeHeight(root.right))