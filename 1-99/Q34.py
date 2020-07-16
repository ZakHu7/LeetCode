class Solution:
    def searchRange(self, nums, target):
        ans = None
        if not nums: return [-1 ,-1]

        if nums[0] <= target <= nums[-1]:
            ans = self.searchRangeR(nums, target, 0 , len(nums) - 1)
        return ans if ans else [-1 ,-1]

    def searchRangeR(self, nums, target, start, end):
        if nums[start] == target and nums[end] == target:
            return [start, end]
        elif start == end:
            return None
        else:
            mid = (start + end) // 2
            firstHalf = None
            secondHalf = None
            if target <= nums[mid]:
                firstHalf = self.searchRangeR(nums, target, start, mid)
            if target >= nums[mid + 1]:
                secondHalf = self.searchRangeR(nums, target, mid + 1, end)
            
            if firstHalf and secondHalf:
                return [firstHalf[0], secondHalf[1]]
            elif firstHalf:
                return firstHalf
            elif secondHalf:
                return secondHalf
            else:
                return None

s = Solution()
nums = [2]

print(s.searchRange(nums, 3))
            

