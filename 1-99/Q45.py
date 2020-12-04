from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 1
        curInd = 0
        jumpLength = nums[curInd]
        while curInd+jumpLength < len(nums)-1:
          count += 1
          nextInd = max(i + nums[i] for i in range(curInd, curInd+jumpLength))
          curInd = nextInd
          jumpLength = nums[curInd]
        return count

s = Solution()
print(s.jump([2,1,1,1,1]))