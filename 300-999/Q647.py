class Solution:
  def countSubstrings(self, s: str) -> str:
    res = 0
    def longestPalindromeH(left, right):
      if left < 0 or right >= len(s) or s[left] != s[right]:
        return 0
      return 1+longestPalindromeH(left-1, right+1)
    
    for i in range(len(s)):
      res += longestPalindromeH(i, i+1)
      res += longestPalindromeH(i-1, i+1)
    return res+len(s)