# House Robber
class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        sums = [nums[0], nums[1], nums[0] + nums[2]]

        for i in range(3, len(nums)):
            sums.append(max(sums[i - 2], sums[i - 3]) + nums[i])

        return max(sums[len(sums) - 2 - 1:])

s = Solution()
nums = [7,4,5,7,2,1,3,6,10,15,1,3,5,6,20]

print(s.rob(nums))


        