from typing import List
from collections import deque
class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    d = set(wordDict)
    dp = [[True,[[]]]] + [[False,[]] for _ in range(len(s))]

    for i in range(len(s)):
      for j in range(i+1, len(s)+1):
        word = s[i:j]
        if s[i:j] in wordDict and dp[i][0]:
          dp[j][0] = True
          for prevGroup in dp[i][1]:
            dp[j][1].append(prevGroup + [word])
    
    return [" ".join(group) for group in dp[len(s)][1]]
    # res = []
    # queue = deque()
    # for word in dp[len(s)][1]:
    #   queue.append([word, '', len(s)])
    # while queue:
    #   curWord, soFar, curInd = queue.popleft()
    #   soFar = " ".join([curWord, soFar])
    #   nextInd = curInd-len(curWord)
    #   if nextInd == 0:
    #     res.append(soFar.strip())
    #   else:
    #     for nextWord in dp[nextInd][1]:
    #       queue.append([nextWord, soFar, nextInd])
    # return res

sol = Solution()
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(sol.wordBreak(s, wordDict))