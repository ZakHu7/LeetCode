from typing import List
class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
      for n in coins:
        if i - n < 0:
          continue
        dp[i] = min(dp[i], dp[i-n]+1)
    return -1 if dp[amount] == float("inf") else dp[amount]
