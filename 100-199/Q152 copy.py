from typing import List
class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    if not nums:
        return -1
    maxProd, minProd = nums[0], nums[0]
    res = nums[0]
    for n in nums[1:]:
        candidates = (n, maxProd * n, minProd * n)
        maxProd = max(candidates)
        minProd = min(candidates)
        res = max(res, maxProd)
    return res

s = Solution()
nums = [-4,-3,-2]
print(s.maxProduct(nums))
    # [-3,5,-2,3,-1,0,9]
    # [5,-2,3,-1,0,9]
    # [5,2,3,1,0,9]
    # [-2,0,-1]
    # [2,3,-2,4]