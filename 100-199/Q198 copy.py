from typing import List
class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0
    prev2, prev1 = 0, 0
    res = 0

    for i in range(len(nums)):
      res = max(nums[i] + prev2, prev1)
      prev2 = prev1
      prev1 = res

    return res
# from typing import List
# class Solution:
#   def rob(self, nums: List[int]) -> int:
#     dp = [-1] * len(nums) # dp[i] max money at index i

#     def robH(nums, i):
#       if i < 0:
#         return 0
#       if dp[i] >= 0:
#         return dp[i]
#       if i == 0:
#         dp[i] = nums[i]
#       else:
#         dp[i] = max(robH(nums, i-1), nums[i] + robH(nums, i-2))
#       return dp[i]
    
#     return robH(nums, len(nums)-1)