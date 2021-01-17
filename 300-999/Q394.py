from collections import deque
class Solution:
  def decodeString(self, s: str) -> str:
    nums = deque()
    letters = deque()
    
    substring = ""
    number = ""
    for i in range(len(s)):
      if s[i] == "[":
        nums.append(number)
        letters.append(substring)
        substring = ""
        number = ""
      elif s[i] == "]":
        prevSubstring = letters.pop()
        substring = prevSubstring + substring * int(nums.pop())
      elif s[i].isdigit():
        number += s[i]
      elif s[i].isalpha():
        substring += s[i]
      
    return substring