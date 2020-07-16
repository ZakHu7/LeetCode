class Solution:
    ## number of people who trust peopleTrust[n]
    def findJudge(self, N, trust):
        if not trust:
            return 1

        peopleTrust = [0 for _ in range(N + 1)]

        for i in range(len(trust)):
            peopleTrust[trust[i][0]] -= 1
            peopleTrust[trust[i][1]] += 1
        
        for i in range(N + 1):
            if peopleTrust[i] == N - 1:
                return i

        return -1

s = Solution()

N = 2
trust = [[1,2]]

print(s.findJudge(N, trust))
