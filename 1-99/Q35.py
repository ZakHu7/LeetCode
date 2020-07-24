#Search for where element is, or where it would be if it was in the array

#binary search

class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        l, r, m = 0, len(nums)-1, 0

        if not nums: return 0

        while l < r:
          m = l + (r-l)//2

          if nums[m] == target:
            return m
          elif target > nums[m]:
            l = m + 1
          else:
            r = m
        if nums[l] == target or target < nums[l]:
          return l

        return l + 1

    ## better solution with less duplication
    def searchInsert2(self, nums: [int], target: int) -> int:
        l, r, m = 0, len(nums)-1, 0

        while l <= r:
          m = l + (r-l)//2

          if nums[m] == target:
            return m
          elif target > nums[m]:
            l = m + 1
          else:
            r = m - 1

        return l

s = Solution()
nums = [1,3,5,6]
target = 2

print(s.searchInsert(nums, target))