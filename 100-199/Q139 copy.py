from typing import List
class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    d = set(wordDict)
    dp = [True] + [False] * (len(s)-1)

    for i in range(len(s)):
      for j in range(i+1, len(s)+1):
        if s[i:j] in wordDict and dp[i]:
          if j == len(s):
            return True
          dp[j] = True
    return False

# from typing import List
# class Solution:
#   def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#     d = set(wordDict)
#     startSet = set([0])

#     while startSet:
#       start = min(startSet)
#       for i in range(start, len(s)):
#         if s[start:i+1] in d:
#           if i+1 == len(s):
#             return True
#           startSet.add(i+1)
#       startSet.remove(start)
#     return False

word = 'catsandog'
wordDict = ["cats","dog","sand","and","cat"]
s = Solution()

print(s.wordBreak(word, wordDict))