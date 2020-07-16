## unsolved
class Solution:
    def grayCode(self, n: int) -> [int]:
        if not n:
            return [0]
        
        res = []
        for i in range(2**n):
            val = 0
            for j in range(n):
                if (i // (2**j)) % 4 == 1 or (i // (2**j)) % 4 == 2:
                    val += 2**j
            res.append(val)

        return res

s = Solution()

print(s.grayCode(2))
            
                
        
        # 0000
        # 0001
        # 0011
        # 0010
        # 0110
        # 0111
        # 0101
        # 0100
        # 1000
        # 1001
        # 1011
        # 1010
        # 1110
        # 1111
        # 1101
        # 1100