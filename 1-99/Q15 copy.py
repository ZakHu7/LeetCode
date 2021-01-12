from typing import List
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    for i in range(len(nums)-2):
      if i != 0 and nums[i] == nums[i-1]:
        continue
      v1 = nums[i]
      if v1 > 0:
        break
      l, r = i+1, len(nums)-1
      while l < r:
        if nums[l] + nums[r] < -v1:
          l += 1
        elif nums[l] + nums[r] > -v1:
          r -= 1
        else:
          res.append([v1, nums[l], nums[r]])
          l += 1
          r -= 1
          while l < r and nums[l] == nums[l-1]:
            l += 1
          while l < r and nums[r] == nums[r+1]:
            r -= 1

    return res

s = Solution()
nums = [-2,0,1,1,2]
print(s.threeSum(nums))

  # [-1,0,1,2,-1,-4]
  # [-4,-1,-1,0,1,2]