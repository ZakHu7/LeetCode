from typing import List
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    d = {}
    res = 0
    for n in nums:
      if n in d:
        continue
      l = 0
      if n-1 in d and n+1 in d:
        l = d[n-1] + 1 + d[n+1]
        d[n-d[n-1]] = l
        d[n+d[n+1]] = l
        d[n] = l
      elif n-1 in d:
        l = d[n-1]+1
        d[n] = l
        d[n-d[n-1]] = d[n]
      elif n+1 in d:
        l = d[n+1]+1
        d[n] = l
        d[n+d[n+1]] = d[n]
      else:
        l = 1
        d[n] = l
      res = max(res, l)
    return res
  
s = Solution()
nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
print(s.longestConsecutive(nums))