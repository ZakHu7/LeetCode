# from collections import deque
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
#         if not endWord in wordList:
#             return 0
        
#         s = set()
#         for word in wordList:
#             s.add(word)

#         q = deque([beginWord])
#         ans = 1

#         while q:
#             ans += 1
#             for _ in range(len(q)):
#                 word = q.popleft()
#                 for i in range(len(word)):
#                     l = word[:i]
#                     r = word[i+1:]
#                     for c in range(ord('a'), ord('z') + 1):
#                         newWord = l + chr(c) + r
#                         if newWord == endWord:
#                             return ans
#                         if newWord in s:
#                             s.remove(newWord)
#                             q.append(newWord)                    

#         return 0

from collections import deque
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
	        return 0
        wordSet.remove(endWord)
        queueFront = deque([beginWord])
        queueBack = deque([endWord])
        visitedFrontSet = set()
        visitedBackSet = set([endWord])
        count = 2
        while len(queueFront) > 0 and len(queueBack) > 0:
            for i in range(len(queueFront)):
                curWord = queueFront.popleft()
                for i in range(len(curWord)):
                    for j in range(26):
                        if curWord[i] == chr(ord('a') + j): continue
                        newWord = curWord[0:i] + chr(ord('a') + j) + curWord[i+1:]
                        if newWord in visitedBackSet:
                            return count
                        if newWord in wordSet:
                            queueFront.append(newWord)
                            visitedFrontSet.add(newWord)
                            wordSet.remove(newWord)
            count += 1
            for i in range(len(queueBack)):
                curWord = queueBack.popleft()
                for i in range(len(curWord)):
                    for j in range(26):
                        if curWord[i] == chr(ord('a') + j): continue
                        newWord = curWord[0:i] + chr(ord('a') + j) + curWord[i+1:]
                        if newWord in visitedFrontSet:
                            return count
                        if newWord in wordSet:
                            queueBack.append(newWord)
                            visitedBackSet.add(newWord)
                            wordSet.remove(newWord)
            count += 1
        return 0



s = Solution()
beginWord = "leet"
endWord = "code"
wordList = ["lest","leet","lose","code","lode","robe","lost"]

# "leet"
# "code"
# ["lest","leet","lose","code","lode","robe","lost"]

print(s.ladderLength(beginWord, endWord, wordList))