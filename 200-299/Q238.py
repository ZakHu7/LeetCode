# Produce of Array Except Self
class Solution:
    # nums: list[int]
    # return list[int]
    def productExceptSelf(self, nums):
        # products of numbers from right to left
        rightToLeft = [1]
        for i in range(len(nums) - 1):
            rightToLeft.append(rightToLeft[i] * nums[len(nums) - i - 1])
        print(rightToLeft)

        leftToRight = 1
        res = []
        for i in range(len(nums)):
            res.append(rightToLeft[len(rightToLeft) - i - 1] * leftToRight)
            leftToRight *= nums[i]
        
        return res

s = Solution()
nums = [3,1,7,2,5,4]

print(s.productExceptSelf(nums))