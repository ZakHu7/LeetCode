class Solution:
    def singleNumber(self, nums: [int]) -> int:
        ones = 0
        twos = 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = twos ^ nums[i] & ~ones
        return ones


nums = [0,1,0,1,0,1]
s = Solution()

print(s.singleNumber(nums))