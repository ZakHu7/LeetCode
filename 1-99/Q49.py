## Group anagrams together in array of strings
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# first soln. take string. isAnagram.
#   to compare, every char match, remove char from both. remove all matched strings.
#   O(nlogn + ns), n is size of array s is length of string(assume same)
#   TOO SLOW. sorted strs first? still slow

# second soln. sort string by ascii value. use map
# O(slogs*n)

# best. count number of occurences of each letter. in tuple of size 26
#   then use map. time O(s*n), space O(s*n)

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        sortedStrs = sorted(strs, key = len)
        ret = []
        while sortedStrs:
            s = sortedStrs[-1]
            sortedStrs = sortedStrs[:-1]
            ret.append([s])
            for i in range(len(sortedStrs) - 1, -1, -1):
                t = sortedStrs[i]
                if len(t) != len(s):
                    break
                if self.isAnagram(s,t):
                    ret[-1].append(t)
                    sortedStrs.remove(t)
        return ret
    
    def isAnagram(self, s1, s2):
        if len(s1) != len(s2):
            return False
        for c in s1:
            if c in s2:
                s2 = s2.replace(c, "", 1) ## alternative find first occurence of c, then substring
                continue
            return False
        return True

            
s = Solution()        
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["abc", "acb", "bac", "bca", "cab", "cba"]
# strs = ["a", "aa", "bb", "ac", "ca", "bb"]
# strs = ["fee", "fed", "def", "dee", "dff", "bb"]
print(s.groupAnagrams(strs))
# print(strs)