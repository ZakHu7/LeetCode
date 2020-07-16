class Solution:
    def findMin(self, nums: [int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[l] < nums[r]:
                return nums[l]
            elif nums[l] > nums[m]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                return -1
        return nums[l]

s = Solution()
nums1 = [4,5,6,7,0,1,2]
nums2 = [0,1,2,3,4,5,6]
nums3 = [6,0,1,2,3,4,5]
nums4 = [4,5,7,0,1,2,3]
print(s.findMin(nums1))
print(s.findMin(nums2))
print(s.findMin(nums3))
print(s.findMin(nums4))