from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permuteH([], nums)
    
    def permuteH(self, soFar, nums):
      if not nums:
        return [soFar]
      res = []
      for i, n in enumerate(nums):
        res += self.permuteH(soFar + [n], nums[0:i]+nums[i+1:])
      return res
  

s = Solution()
nums = [1,2,3]
print(s.permute(nums))
