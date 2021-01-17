from collections import deque
class Solution:
  def isValid(self, s: str) -> bool:
    stack = deque()
    for p in s:
      if p in ["(", "{", "["]:
        stack.append(p)
      else:
        if not stack:
          return False
        start = stack.pop()
        if not ((start == "(" and p == ")")
          or (start == "{" and p == "}")
          or (start == "[" and p == "]")):
          return False
    return not stack