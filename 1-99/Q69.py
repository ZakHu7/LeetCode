class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        low, high = 1, x

        while low < high:
            mid = (low + high) // 2

            if x // mid >= mid and x // (mid + 1) < (mid + 1):
                return mid
            elif x // mid < mid:
                high = mid
            else:
                low = mid
        
        return -1

        

s = Solution()

print(s.mySqrt(4))