## implement kmp algorithm
## run-time O(n + m) n is length of haystack, m is length of needle
## space O(m)

## think of dfa, and failure states.

class Solution:
  def makeFailureArray(self, needle):
    i, j = 1, 0
    arr = [0] * len(needle)

    while i < len(needle):
      if needle[j] == needle[i]:
        j += 1
        arr[i] = j
        i += 1
      else:
        if j > 0:
          j = arr[j-1]
        else:
          arr[i] = j ## j is 0
          i += 1
    return arr

  def strStr(self, haystack: str, needle: str) -> int:
    if not needle: return 0
    failureArr = self.makeFailureArray(needle)
    i, j = 0, 0

    while i < len(haystack):
      if haystack[i] == needle[j]:
        if j == len(needle) - 1:
          return i - len(needle) + 1
        i += 1
        j += 1
      else:
        if j > 0:
          j = failureArr[j-1]
        else:
          i += 1
    return -1
      
s = Solution()
haystack = "aaabaaabaaaa"
needle = "bba"

print(s.strStr(haystack, needle))
