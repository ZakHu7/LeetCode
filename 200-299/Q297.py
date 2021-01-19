# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

from collections import deque
class Codec:

  def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    lst = []
    def serializeH(root):
      if root:
        lst.append(str(root.val))
        serializeH(root.left)
        serializeH(root.right)
      else:
        lst.append('#')
    serializeH(root)
    return ''.join(lst)

  def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    nodes = deque(data)
    def deserializeH(nodes):
      val = nodes.popleft()
      if val == '#':
        return None
      node = TreeNode(int(val))
      node.left = deserializeH(nodes)
      node.right = deserializeH(nodes)
      return node
    return deserializeH(nodes)
      
    
        
    
    
s = Codec()
root = TreeNode(1,  TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
print(s.serialize(root))
a = s.deserialize(s.serialize(root))
print("damn")

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))