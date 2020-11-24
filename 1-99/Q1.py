from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
          if target - nums[i] in dictionary:
            return [dictionary[target-nums[i]], i]
          dictionary[nums[i]] = i
        return -1

s = Solution()

nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))

nums = [3,2,4]
target = 6
print(s.twoSum(nums, target))

nums = [3,3]
target = 6
print(s.twoSum(nums, target))
