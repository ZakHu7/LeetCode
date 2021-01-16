class Solution:
  def minWindow(self, s: str, t: str) -> str:
    d = {}
    notFound = len(t)
    for c in t:
      if c in d:
        d[c] += 1
      else:
        d[c] = 1
    start, end, minStart, minEnd = 0, 0, 0, float('inf')
    while end < len(s):
      if s[end] in d:
        d[s[end]] -= 1
        if d[s[end]] >= 0:
          notFound -= 1
      if not notFound:
        while True:
          if s[start] in d:
            if d[s[start]] == 0:
              break
            d[s[start]] += 1
          start += 1
        if end - start < minEnd - minStart:
          minStart, minEnd = start, end
        
        d[s[start]] += 1
        start += 1
        notFound += 1
      end += 1
    if minEnd == float('inf'):
      return ""
    return s[minStart:minEnd+1]



# class Solution:
#   def minWindow(self, s: str, t: str) -> str:
#     def letterToIndex(c):
#       if c.isupper():
#         return ord(c)-ord('A')
#       return ord(c)-ord('a')+26

#     tLetters = [0] * 52
#     tSet = set(t)
#     notFound = len(t)
#     for c in t:
#       if c.isupper():
#         tLetters[letterToIndex(c)] += 1
#       else:
#         tLetters[letterToIndex(c)] += 1
#     end = 0

#     # finds first letter of s in t
#     # s=DDDA  t=A
#     while end < len(s):
#       if tLetters[letterToIndex(s[end])] > 0:
#         break
#       end += 1
#     start = end
    
#     minWindow = (0, float('inf'))
#     while end < len(s):
#       while notFound > 0 and end < len(s):
#         if tLetters[letterToIndex(s[end])] > 0:
#           notFound -= 1
#         if s[end] in tSet:
#           tLetters[letterToIndex(s[end])] -= 1
#         end += 1
#       if notFound == 0:
#         if tLetters[letterToIndex(s[start])] < 0:
#           while start < end:
#             if s[start] in tSet and tLetters[letterToIndex(s[start])] == 0:
#               break
#             if s[start] in tSet:
#               tLetters[letterToIndex(s[start])] += 1
#             start += 1
#         if end - start < minWindow[1] - minWindow[0]:
#           minWindow = (start, end)

#         tLetters[letterToIndex(s[start])] += 1
#         notFound += 1
#         start += 1
        
#         while start < end:
#           if s[start] in tSet and tLetters[letterToIndex(s[start])] >= 0:
#             break
#           if s[start] in tSet:
#             tLetters[letterToIndex(s[start])] += 1
#           start += 1

#     if minWindow[1] == float('inf'):
#       return ""
#     return s[minWindow[0]:minWindow[1]]

sol = Solution()
s = "aa"

t = "aa"
print(sol.minWindow(s, t))

# BCBCCCABA