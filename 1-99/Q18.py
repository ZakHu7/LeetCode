from typing import List
class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    res = []
    for j in range(len(nums)-3):
      if j != 0 and nums[j] == nums[j-1]:
        continue
      for i in range(j+1, len(nums)-2):
        if i != j+1 and nums[i] == nums[i-1]:
          continue
        left, right = i+1, len(nums)-1
        while left < right:
          total = nums[j] + nums[i] + nums[left] + nums[right]
          if total == target:
            res.append([nums[j], nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left-1]:
              left += 1
            while left < right and nums[right] == nums[right+1]:
              right -= 1
          elif total > target:
            right -= 1
          else:
            left += 1

    return res
  
s = Solution()
nums = [1,0,-1,0,-2,2] # -2 -1 0 0 1 2
target = 0
print(s.fourSum(nums, target))