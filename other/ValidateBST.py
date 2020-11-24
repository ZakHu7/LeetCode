from binarytree import tree, bst

## better would be instead of passing up the min/max, pass down the min and max
## would not need to return multiple things

def validateBST(node):
  if not node:
    return float('-inf'), float('inf'), True
  leftMax, leftMin, leftErr = validateBST(node.left)
  rightMax, rightMin, rightErr = validateBST(node.right)

  if not leftErr or not rightErr:
    return 0, 0, False
  if leftMax > node.val or node.val > rightMin:
    return 0, 0, False
  return max(node.val, rightMax), min(node.val, leftMin), True

tree = tree(height=3)

print(tree)

_,_,c = validateBST(tree)
print(c)