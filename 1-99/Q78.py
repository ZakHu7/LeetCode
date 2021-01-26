from typing import List
class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = [[]]
    for n in nums:
      l = len(res)
      for i in range(l):
        cur = res[i]
        res.append(cur+[n])
    return res