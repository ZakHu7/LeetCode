class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if not nums:
            return 0

        ans = 1
        cur = replace = 1

        last = nums[0]
        count = 1
        while replace < len(nums):
            if last == nums[cur] and count == 2:
                ##
            elif last == nums[cur]:
                count += 1
                cur += 1
                


        return ans