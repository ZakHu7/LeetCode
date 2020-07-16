class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            first =  -float("inf") if m == 0 else nums[m - 1]
            second = nums[m]
            third = -float("inf") if m == len(nums) - 1 else nums[m + 1]

            if first < second > third:
                return m
            elif first < second < third:
                l = m + 1
            else:
                r = m - 1

        return -1

s = Solution()
nums = [1,2,1,3,5,6,4]
print(s.findPeakElement(nums))