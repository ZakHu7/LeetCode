from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        if not nums:
            return []
        if k == 1:
            return nums

        window = deque([nums[0]])
        ans = []

        for i in range(1, len(nums)):
            lastAppended = window.pop()
            while nums[i] > lastAppended:
                if len(window) == 0:
                    lastAppended = None
                    break
                lastAppended = window.pop()
            
            if lastAppended:
                window.append(lastAppended)
            window.append(nums[i])

            if len(window) > k:
                window.popleft()
            
            if i + 1 >= k:
                ans.append(window[0])
        
        return ans
    
s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(s.maxSlidingWindow(nums, k))
