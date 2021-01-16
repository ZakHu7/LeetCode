class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # abcdbe abcdb
    res = 0
    seen = {}
    start = 0

    for i, c in enumerate(s):
      if c in seen and seen[c] >= start:
        start = seen[c] + 1
      
      seen[c] = i
      res = max(res, i-start+1)

    return res