from typing import List
from random import shuffle
class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    def partition(lo, hi, nums):
      i = lo
      for j in range(lo, hi):
        if nums[j] <= nums[hi]:
          nums[i], nums[j] = nums[j], nums[i]
          i += 1
      nums[i], nums[hi] = nums[hi], nums[i]
      return i
    
    
    shuffle(nums)
    k = len(nums) - k
    left, right = 0, len(nums)-1
    i = 0
    while left < right:
      i = partition(left, right, nums)
      if i == k:
        break
      elif i < k:
        left = i+1
      else:
        right = i-1
    return nums[k]
          