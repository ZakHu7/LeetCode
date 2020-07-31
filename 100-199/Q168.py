## count every 26^i

class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = ""

        while(n > 0):
          ret = chr(ord('A') + (n-1)%26) + ret
          n = (n-1) // 26
        
        return ret


s = Solution()
n = 53
print(s.convertToTitle(n))