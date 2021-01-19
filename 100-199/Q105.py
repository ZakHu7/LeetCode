# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
from typing import List
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTreeH(preS, preE, inS, inE):
      if preS > preE or inS > inE:
        return None
      node = TreeNode(preorder[preS])
      index = inorder.index(node.val)
      node.left = buildTreeH(preS+1, preS+index-inS, inS, index-1)
      node.right = buildTreeH(preS+index+1-inS, preE, index+1, inE)
      return node
    
    return buildTreeH(0, len(preorder)-1, 0, len (inorder)-1)
    