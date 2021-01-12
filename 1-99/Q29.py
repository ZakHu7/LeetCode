class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    if dividend == 0:
      return 0
    neg = 1
    if dividend < 0:
      dividend *= -1
      neg *= -1
    if divisor < 0:
      divisor *= -1
      neg *= -1
    
    res, _ = self.divideH(dividend, divisor, 1, neg)
    return res * neg
    
  def divideH(self, dividend, divisor, multiple, neg):
    res = 0
    remain = dividend
    nextMultiple = multiple

    if dividend >= divisor * multiple:
      if multiple >= 2**31-1:
        return multiple, 0
      if (2**31-1)//2 + 1 <= multiple and neg == 1:
        nextMultiple = 2**31-1
      elif (2**31)//2 <= multiple and neg == -1:
        nextMultiple = 2**31
      else:
        nextMultiple *= 2
      soFar, remain = self.divideH(dividend, divisor, nextMultiple, neg)
      res += soFar
      if remain >= divisor * multiple:
        res += multiple
        remain -= divisor*multiple
    return res, remain


s = Solution()
a = -2147483648
b = 1
# a = 10
# b = 3
print(s.divide(a, b))