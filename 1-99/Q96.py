class Solution:
    def numTrees(self, n):
        dyn = [None] * (n+1)
        dyn[0] = 1
        dyn[1] = 1
        return self.numTreesH(dyn,n)

    def numTreesH(self, dyn, n):
        if dyn[n] != None:
            return dyn[n]
        else:
            sum = 0
            for i in range(n):
                sum += self.numTreesH(dyn,i) * self.numTreesH(dyn,n-i-1)
            dyn[n] = sum
            return dyn[n]



        
s = Solution()

print(s.numTrees(3))