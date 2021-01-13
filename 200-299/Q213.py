from typing import List
class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) <= 3:
      return max(nums)
    res1, res2 = 0 ,2

    prev2, prev1 = 0, 0
    for i in range(len(nums) - 1):
      res1 = max(prev1, prev2 + nums[i])
      prev2 = prev1
      prev1 = res1

    prev2, prev1 = 0, 0
    for i in range(1, len(nums)):
      res2 = max(prev1, prev2 + nums[i])
      prev2 = prev1
      prev1 = res2

    return max(res1, res2)

    # 1 2 1 0
    #   2 2
    # 3, 4, 4 = max(prev1, prev2 + nums[i], prev2 + nums[0])
