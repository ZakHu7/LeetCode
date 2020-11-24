class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        startInd = 0
        maxLength = 0
        curLength = 0

        for i, char in enumerate(s):
          if char not in lastSeen:
            lastSeen[char] = i
            curLength += 1
          else:
            if lastSeen[char] < startInd:
              lastSeen[char] = i
              curLength += 1
            else:
              startInd = lastSeen[char]
              curLength = i - startInd
              lastSeen[char] = i
          maxLength = max(maxLength, curLength)

        return maxLength


s = Solution()
s1 = "abcabcbb"
print(s.lengthOfLongestSubstring(s1))

s1 = "bbbbb"
print(s.lengthOfLongestSubstring(s1))

s1 = "pwwkew"
print(s.lengthOfLongestSubstring(s1))

s1 = ""
print(s.lengthOfLongestSubstring(s1))

s1 = "abcdba"
print(s.lengthOfLongestSubstring(s1))

s1 = "abababababa"
print(s.lengthOfLongestSubstring(s1))
