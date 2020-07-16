class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # store the largest positive and negative product at all times
        pos = 0
        neg = 0
        largest = nums[0]

        for i in range(len(nums)):
            val = nums[i]

            pos *= val
            neg *= val

            if val < 0:
                pos, neg = neg, pos

            if val > 0 and pos == 0:
                pos = val
            elif val < 0 and neg == 0:
                neg = val

            largest = max(largest, pos, neg)

        return largest
            

s = Solution()

nums = [-2]

print(s.maxProduct(nums))

