class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ## remove the largest number before the slope is negative
        if len(num) == k:
            return "0"

        peak = 0

        while k > 0:   
            if peak == len(num) - 1:
                num = num[:-k]   
                k = 0          
            elif num[peak] > num[peak + 1]:
                num = num[:peak] + num[peak+1:]
                peak = max(peak - 1, 0)
                k -= 1
            elif num[peak] <= num[peak + 1]:
                peak += 1

        while len(num) > 1 and num[0] == "0":
            num = num[1:]
        
        return num

s = Solution()
num = "23746789"
k = 6

print(s.removeKdigits(num, k))
            
                

            