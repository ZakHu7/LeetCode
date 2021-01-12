from typing import List
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    res, soFar = float('-inf'), 0
    for n in nums:
      soFar += n
      res = max(soFar, res)
      soFar = max(soFar, 0)
    return res