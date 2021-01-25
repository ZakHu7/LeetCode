from typing import List
class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    closestOffset = float('inf')
    for i in range(len(nums)):
      left, right = i+1, len(nums)-1
      
      while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total == target:
          return target
        elif total > target:
          right -= 1
        else:
          left += 1
        if abs(total-target) < abs(closestOffset):
          closestOffset = total-target

    return target+closestOffset