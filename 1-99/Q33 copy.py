from typing import List
class Solution:
  def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l < r:
      m = l + (r-l)//2
      if target == nums[m]:
        return m
      if nums[l] <= nums[m]:
        if nums[l] <= target <= nums[m]:
          r = m
        else:
          l = m+1
      elif nums[m] <= nums[r]:
        if nums[m] <= target <= nums[r]:
          l = m
        else:
          r = m-1
    return l if nums[l] == target else -1

s = Solution()
nums = [1,3]
target = 2
print(s.search(nums, target))