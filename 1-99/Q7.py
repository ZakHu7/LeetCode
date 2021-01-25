class Solution:
  def reverse(self, x: int) -> int:
    res = 0
    neg = 1
    maxInt = 2**31
    if x < 0:
      neg = -1
      x *= -1
    while x:
      n = x%10
      if neg == -1 and (maxInt - n)//10 < res:
        return 0
      elif (maxInt-1 - n)//10 < res:
        return 0
      res = res*10 + n
      x //= 10
      
    return neg * res
  
# class Solution:
#   def reverse(self, x: int) -> int:
#     res = 0
#     power = 0
#     neg = 1
#     if x < 0:
#       neg = -1
#       x *= -1
#     for n in str(x):
#       newNum = int(n) * 10**power
#       if neg == -1 and (2**31 - newNum) < res:
#         return 0
#       elif (2**31-1 - newNum) < res:
#         return 0
#       res += newNum
#       power += 1
      
#     return neg * res
  
s = Solution()
x = -123
print(s.reverse(x))