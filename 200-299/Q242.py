class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    d = [0] * 26
    for c in s:
      d[ord(c)-ord('a')] += 1
    for c in t:
      d[ord(c)-ord('a')] -= 1
    for n in d:
      if n != 0:
        return False
    return True