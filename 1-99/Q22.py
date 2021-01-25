from typing import List
from collections import deque
class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    queue = deque()
    res = []
    queue.append(([], n, n))
    while queue:
      soFar, openP, closedP = queue.popleft()
      if not openP and not closedP:
        res.append("".join(soFar))
        continue
      if openP:
        queue.append((soFar+['('], openP-1, closedP))
      if closedP > openP:
        queue.append((soFar+[')'], openP, closedP-1))
    
    # def generateParenthesisH(res, soFar, openP, closedP):
    #   if not openP and not closedP:
    #     res.append(soFar)
    #     return
    #   if openP:
    #     generateParenthesisH(res, soFar+'(', openP-1, closedP)
    #   if closedP > openP:
    #     generateParenthesisH(res, soFar+')', openP, closedP-1)
    # generateParenthesisH(res, '', n, n)
    return res
    