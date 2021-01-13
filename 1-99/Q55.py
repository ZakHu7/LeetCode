from typing import List
class Solution:
  def canJump(self, nums: List[int]) -> bool:
    maxDistance = 0

    for i in range(len(nums)):
      if i > maxDistance:
        break
      if i == len(nums) - 1:
        return True
      maxDistance = max(maxDistance, i + nums[i])
      
    return False

  
# 10 9 8 7 6 5 4 3 2 1 0 0