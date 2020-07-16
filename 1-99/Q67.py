class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        buffer = ""
        if len(a) > len(b):
            for _ in range(len(a) - len(b)):
                buffer += "0"
            b = buffer + b
        else:
            for _ in range(len(b) - len(a)):
                buffer += "0"
            a = buffer + a

        carry = 0
        ans = ""

        for i in range(maxLen):
            val = int(a[maxLen - i - 1]) + int(b[maxLen - i - 1]) + carry
            carry = val // 2

            ans = str(val % 2) + ans

        if carry == 1:
            ans = "1" + ans
        
        return ans

s = Solution()

a = "101"
b = "11"

print(s.addBinary(a, b))