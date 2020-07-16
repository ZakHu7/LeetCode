# Word Break
class Solution:
    def wordBreak(self, s, wordDict):
        startIndexes = set()
        startIndexes.add(0)

        # for end in range(1, len(s) + 1):
        #     for start in startIndexes:
        #         if s[start:end] in wordDict:
                    # if end == len(s):
                    #     return True
        #             startIndexes.append(end)
        while startIndexes:
            start = min(startIndexes)
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    if end == len(s):
                        return True
                    startIndexes.add(end)
            startIndexes.remove(start)
            


        return False


s = Solution()

word = "catsandog"
wordDict = ["cats", "sand", "and", "dog", "cat", "an"]

# word = "aaaaab"
# wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa"]
print(s.wordBreak(word, wordDict))