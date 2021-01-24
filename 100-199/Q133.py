# Definition for a Node.
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

from collections import deque
class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
      return None
    nodes = {}
    copyNode = Node(node.val)
    queue = deque([(node, copyNode)])
    nodes[node.val] = copyNode
    while queue:
      (old, copy) = queue.popleft()
      for neighbor in old.neighbors:
        if neighbor.val not in nodes:
          newNeighbor = Node(neighbor.val)
          queue.append((neighbor, newNeighbor))
          nodes[neighbor.val] = newNeighbor
          copy.neighbors.append(newNeighbor)
        else:
          copy.neighbors.append(nodes[neighbor.val])
          
          
    return copyNode
        