class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1, 1]

        fibLen = 0
        ans = 1

        
        def fib(n) -> int:
            if n >= len(dp):
                for _ in range(n - len(dp) + 1):
                    dp.append(dp[-1] + dp[-2])

            return dp[n]

        for i in range(len(s) + 1):
            if i < len(s) and s[i] == "0" and (i == 0 or s[i - 1] >= "3" or s[i - 1] == "0"):
                return 0
            elif i < len(s) and s[i] == "0":
                fibLen = max(fibLen - 1, 0)
            elif i < len(s) and ("1" == s[i - 1] or (s[i - 1] == "2" and s[i] <= "6")):
                fibLen += 1
            else:
                ans *= fib(fibLen)
                fibLen = 1

        return ans

s = Solution()
string = "27"

print(s.numDecodings(string))