from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        if not endWord in wordList:
            return 0
        
        s = set()
        for word in wordList:
            s.add(word)

        q = deque([beginWord])
        ans = 1

        while q:
            ans += 1
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    l = word[:i]
                    r = word[i+1:]
                    for c in range(ord('a'), ord('z') + 1):
                        newWord = l + chr(c) + r
                        if newWord == endWord:
                            return ans
                        if newWord in s:
                            s.remove(newWord)
                            q.append(newWord)                    

        return 0

s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

print(s.ladderLength(beginWord, endWord, wordList))