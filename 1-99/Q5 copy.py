class Solution:
  def longestPalindrome(self, s: str) -> str:
    def longestPalindromeH(left, right):
      if left < 0 or right >= len(s) or s[left] != s[right]:
        return (left+1, right-1)
      return longestPalindromeH(left-1, right+1)
    
    res = (0, 0)
    for i in range(len(s)-1):
      substring = longestPalindromeH(i, i+1)
      if res[1]-res[0] < substring[1]-substring[0]:
        res = substring
      substring = longestPalindromeH(i-1, i+1)
      if res[1]-res[0] < substring[1]-substring[0]:
        res = substring
    return s[res[0]: res[1]+1]