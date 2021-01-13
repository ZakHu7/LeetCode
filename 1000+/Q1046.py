class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        stones.sort()

        while len(stones) > 1:
            element = stones[len(stones)-1] - stones[len(stones)-2]  ##Last el - second last el
            stones = stones[:-2]

            stones = self.insertToSorted(stones, element)
        

        return stones[0]


    def insertToSorted(self, stones, element):
        if not stones:
            return [element]
        right = 0
        left = len(stones) - 1
        if element < stones[right]:
            return [element] + stones[:]
        elif element > stones[left]:
            return stones[:] + [element]
        ## in between
        while right + 1 < left:
            mid = right + (left - right) // 2
            if element < stones[mid]:
                left = mid
            elif element >= stones[mid]:
                right = mid
        
        return stones[:left] + [element] + stones[left:]

stones = [2,7,4,1,8,1]
s = Solution()
stones2 = s.lastStoneWeight(stones)
print(stones2)