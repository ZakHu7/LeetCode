class Solution:
    def removeDuplicates(self, nums):
        fastIndex = 1
        slowIndex = 0

        while fastIndex < len(nums):
            if nums[slowIndex] != nums[fastIndex]:
                slowIndex += 1
                nums[slowIndex] = nums[fastIndex]
                
            fastIndex += 1



        return slowIndex + 1



s = Solution()

nums = [1,1,1,2,2,3,5]

v = s.removeDuplicates(nums)

print(v)
print(nums)

