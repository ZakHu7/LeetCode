class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        candidates.sort()
        self.combinationSumH(candidates, ans, [], target, 0)
        return ans
        
    def combinationSumH(self, candidates, ans, soFar, rem, index):
        for i in range(index, len(candidates)):
            cur = candidates[i]
            if rem == 0:
                ans.append(soFar)
                return False
            elif rem < 0:
                return False
            else:
                if not self.combinationSumH(candidates, ans, soFar + [cur], rem - cur, i):
                    return True
        return True

s = Solution()

candidates = [2,3,5]

target = 8

print(s.combinationSum(candidates, target))
        