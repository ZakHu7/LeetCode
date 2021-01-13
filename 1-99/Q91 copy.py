class Solution:
  def numDecodings(self, s: str) -> int:
    if s[0] == "0":
      return 0
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(s)+1):
      single = s[i-1]
      if 1 <= int(single) <= 9:
        dp[i] += dp[i-1]

      double = s[i-2:i]
      if 10 <= int(double) <= 26:
        dp[i] += dp[i-2]
      
    return dp[-1]
s = Solution()
string = "226"
print(s.numDecodings(string))
# class Solution:
#   def numDecodings(self, s: str) -> int:
#     prev2, prev1 = 1, 1
#     res = 0

#     for i in range(len(s)):
#       if s[i] == "0":
#         if i != 0 and (s[i-1] == "1" or s[i-1] == "2"):
#           res = prev2
#         else:
#           return 0
#       elif i != 0 and 10 <= int(s[i-1:i+1]) <= 26:
#         res = prev2 + prev1
#       else:
#         res = prev1
#       prev2 = prev1
#       prev1 = res

#     return res
    # s 2 2 6 1 1 2 7
    # 1 1 2 3 3 6 9
    # 1 1 2

    # s 2 2 6
    # 1 1 2 3