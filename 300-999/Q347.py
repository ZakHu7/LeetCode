from typing import List
import heapq
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    d = {}
    for n in nums:
      if n in d:
        d[n] += 1
      else:
        d[n] = 1
    freqArr = []
    for (key, val) in d.items():
      freqArr.append((-val, key))
    heapq.heapify(freqArr)
    res = []
    for i in range(k):
      res.append(heapq.heappop(freqArr)[1])
    return res
  
