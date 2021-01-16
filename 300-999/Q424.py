class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    majorityCharCount = 0
    start = 0
    letters = [0] * 26
    res = 0
    for end in range(1, len(s)+1):
      charInd = ord(s[end-1]) - ord('A')
      letters[charInd] += 1
      majorityCharCount = max(majorityCharCount, letters[charInd])

      if end - start > majorityCharCount + k:
        letters[ord(s[start])-ord('A')] -= 1
        start += 1
      
      res = max(res, end - start)

    return res
    
# class Solution:
#   def characterReplacement(self, s: str, k: int) -> int:
#     if not s: return 0
#     letters = [0] * 26 # Letter: how many in substring
#     start = 0
#     changedCount = 0
#     majorityChar = ''
#     majorityCharCount = 0
#     res = 0

#     for i, c in enumerate(s):
#       letters[ord(c)-ord('A')] += 1
#       if c == majorityChar:
#         majorityCharCount += 1
#       elif letters[ord(c)-ord('A')] >= majorityCharCount:
#         majorityChar = c
#         majorityCharCount = letters[ord(c)-ord('A')]
#         changedCount = i-start+1-majorityCharCount
#       else:
#         changedCount += 1

#       while changedCount > k:
#         letters[ord(s[start])-ord('A')] -= 1
#         if s[start] == majorityChar:
#           majorityCharCount -= 1
#           for j, count in enumerate(letters):
#             if count > majorityCharCount:
#               majorityChar = chr(j + ord('A'))
#               majorityCharCount = count
#               changedCount = i-start-majorityCharCount
#         else:
#           changedCount -= 1
#         start += 1
#       res = max(res, i-start+1)
#     return res
    
    # AABABBA
    # ABABCD
sol = Solution()
s = "AABABBA"
k = 0
print(sol.characterReplacement(s, k))