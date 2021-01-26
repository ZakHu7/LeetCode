from typing import List
from collections import deque
class Solution:
  def addOperators(self, num: str, target: int) -> List[str]:
    stack = deque()
    stack.append([0, 0, '', ''])
    res = []
    
    while stack:
      ind, val, evalStr, prev = stack.pop()
      if ind == len(num):
        if val == target:
          res.append(evalStr)
      else:
        stack.append([ind+1, val + int(num[ind]), evalStr + '+' +num[ind], '+'])
        stack.append([ind+1, val - int(num[ind]), evalStr + '-' +num[ind], '-'])
        
        if ind != 0:
          stack.append([ind+1, val - int(num[ind]), evalStr + '-' +num[ind], '-'])
          
## skip question