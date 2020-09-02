# class TreeNode:
#   def __init__(self, val, left, right):
#     self.val = val
#     self.left = left
#     self.right = right
#   def preOrder(self):
#     print(self.val)
#     if self.left:
#       self.left.preOrder()
#     if self.right:
#       self.right.preOrder()

from binarytree import Node

class Solution:
  def convertArrayToTreeR(self, arr):
    l = len(arr)
    if l == 0:
      return None
    left = self.convertArrayToTree(arr[:l//2])
    right = self.convertArrayToTree(arr[l//2+1:])
    node = Node(arr[l//2], left, right)

    return node

  def convertArrayToTree(self, arr):
    root = self.convertArrayToTreeR(arr)

    return root

s = Solution()
arr = [1,2,3,4,5,6]

tree = s.convertArrayToTree(arr)
print(tree)

