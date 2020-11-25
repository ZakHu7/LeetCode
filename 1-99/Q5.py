class Solution:
  def longestPalindrome(self, s: str) -> str:
    maxFound = ""
    maxLength = 0
    for i in range(len(s)):
      longestFound = self.longestPalindromeH(s, i-1, i+1, s[i])
      if len(longestFound) > maxLength:
        maxFound = longestFound
        maxLength = len(longestFound)
      longestFound = self.longestPalindromeH(s, i, i+1, "")
      if len(longestFound) > maxLength:
        maxFound = longestFound
        maxLength = len(longestFound)
    return maxFound

  def longestPalindromeH(self, s, left, right, longestFound):
    if left < 0 or right >= len(s):
      return longestFound
    if s[left] == s[right]:
      return self.longestPalindromeH(s, left-1, right+1, s[left]+longestFound+s[right])
    return longestFound


s = Solution()

s1 = "aaaaaab" 
print(s.longestPalindrome(s1))


def foo(s):
  s = ""

s2 = "bob"