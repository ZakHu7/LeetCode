class Solution:
    # sort -> find kth element: nlogn time

    def findKthLargest(self, nums, k):
        if not nums:
            return -1

        nums.sort(reverse=True)
        

        

        return nums[k-1]


s = Solution()
nums = [2,5,1,7,4,4,4,4]

print(s.findKthLargest(nums, 1))