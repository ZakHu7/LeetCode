from typing import List
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
    rightProduct = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = rightProduct * res[i]
        rightProduct *= nums[i]
    return res
