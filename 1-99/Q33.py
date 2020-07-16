class Solution:
    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        ## Find the acual first element in the list
        l, r = 0, len(nums) - 1

        while nums[l] > nums[r]:
            mid = l + (r - l) // 2
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] >= nums[l]:
                l = mid + 1
            
        offset = l

        r = (l - 1 + len(nums)) % len(nums)
        virtualL = 0
        virtualR = len(nums) - 1
        while virtualL < virtualR:
            virtualL = (l - offset + len(nums)) % len(nums)
            virtualR = (r - offset + len(nums)) % len(nums)
            mid = ((virtualL + (virtualR - virtualL) // 2) + offset) % len(nums)

            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1

s = Solution()
nums = [1,4]
target = 1

print(s.search(nums, target))


