# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def inOrder(self, root, travel):
    if not root:
      return
    self.inOrder(root.left, travel)
    travel.append(root.val)
    self.inOrder(root.right, travel)

  def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
      return
    root.right, root.left = root.left, root.right
    self.invertTree(root.right)
    self.invertTree(root.left)

    return root

s = Solution()
root = TreeNode(4,
 TreeNode(2, TreeNode(1), TreeNode(3)),
 TreeNode(7, TreeNode(6), TreeNode(9)))
s.invertTree(root)

travel = []
s.inOrder(root, travel)
print(root)
print(travel)



        