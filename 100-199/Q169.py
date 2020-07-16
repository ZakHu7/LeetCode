class Solution:
    def majorityElement(self, nums):
        d = dict()
        
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            
            if d[n] > len(nums) / 2:
                    return n
            
        # for key in d:
        #     if d[key] > len(nums) / 2:
        #         return d[key]
        return None

s = Solution()
nums = [2,2,2,2,1,1,1,1,2]
print(s.majorityElement(nums))

