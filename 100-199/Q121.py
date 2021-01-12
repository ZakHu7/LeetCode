from typing import List
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if not prices:
      return 0
    res = 0
    buy = prices[0]
    for i in range(0,len(prices)):
      res = max(res, prices[i] - buy)
      buy = min(buy, prices[i])
    return res


s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))