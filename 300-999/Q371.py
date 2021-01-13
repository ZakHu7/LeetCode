class Solution:
  def getSum(self, a: int, b: int) -> int:
    while b != 0:
      c = a ^ b
      b = (a & b) << 1
      a = c
    return a

s = Solution()
a = 7
b = -13
print(s.getSum(a, b))