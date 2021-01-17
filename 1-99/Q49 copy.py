from typing import List
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    d = {}
    
    for s in strs:
      l = [0]*26
      for c in s:
        l[ord(c)-ord('a')] += 1
      t = tuple(l)
      d[t] = d.get(t, []) + [s]
    
    return list(d.values())

s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))