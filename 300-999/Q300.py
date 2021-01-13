# from typing import List
# class Solution:
#   def lengthOfLIS(self, nums: List[int]) -> int:
#     dp = [1] * len(nums)
#     res = 1
#     for i in range(1,len(nums)):
#       for j in range(i-1, -1, -1):
#         if nums[i] > nums[j]:
#           dp[i] = max(dp[i], dp[j] + 1)
#       res = max(res, dp[i])
#     return res
from typing import List
class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    def binSearch(tails, target):
      l, r = 0, len(tails)-1
      while l < r:
        m = l + (r-l)//2
        if n < tails[m]:
          r = m
        elif n > tails[m]:
          l = m + 1
        else:
          return m
      return l

    tails = [nums[0]]
    for n in nums:
      if n > tails[-1]:
        tails.append(n)
      else:
        ind = binSearch(tails, n)
        tails[ind] = n
    return len(tails)