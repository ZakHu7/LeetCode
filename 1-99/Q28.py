# Input: haystack = "hello", needle = "ll"
# Output: 2

# -1 if not found

# O(n) solution can be found with KMP/z-algo
# O(n + m) space, for z array, length of haystack + needle

class Solution:
  ## value at z[i] is the length of prefix of s starting from z[i]
  def getZarr(self, s, z):
    n = len(s)
    
    #[left, right] is the z box
    left, right = 0, 0
    for i in range(1, n): ## first entry is useless since it will always be entire string
      ## need to count manually
      if i > right:
        left, right = i, i
        while right < n and s[right - left] == s[right]:
          right += 1
        z[i] = right - left
        right -= 1
      ## from previous count, can reuse values calculated from before
      else:
        ## consider "abaxabab"
        ## if right = 6, left = 4, i = 5
        ## can reuse the value at s[k] for s[i]
        k = i - left

        ## if value does not exceed the right bound, no need to recalculate
        if z[k] < right - i + 1:
          z[i] = z[k]
        else:
          left = i
          while right < n and s[right - left] == s[right]:
            right += 1
          z[i] = right - left
          right -= 1

  def getZarrFromMemory(self, s, z):
    n = len(s)
    l, r = 0, 0
    for i in range(1, n):
      if i > r: ## naive counting
        l, r = i, i
        while r < n and s[r] == s[r - l]:
          r += 1
        z[i] = r - l
        r -= 1
      else:
        k = i - l
        if s[k] < r - i + 1:
          z[i] = z[k]
        else:
          l = i
          while r < n and s[r] == s[r - l]:
            r += 1
          z[i] = r - l
          r -= 1

  def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) == 0: return 0
    concat = needle + "$" + haystack
    l = len(concat)
    z = [0] * l
    self.getZarr(concat, z)

    for i in range(l):
      if z[i] == len(needle):
        return i - len(needle) - 1

    return -1

  # def strStr(self, haystack: str, needle: str) -> int:
  #   if haystack == needle == "": return 0
  #   for i in range(len(haystack) - len(needle) + 1):
  #     found = True
  #     for j in range(len(needle)):
  #       if haystack[i+j] != needle[j]:
  #         found = False
  #         break
  #     if found: return i
  #   return -1

s = Solution()
haystack = "aaabaaabaaaa"
needle = "aaaa"

print(s.strStr(haystack, needle))
