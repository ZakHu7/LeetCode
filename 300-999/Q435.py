from typing import List
class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals:
      return 0
    sortedIntervals = sorted(intervals, key=lambda x:x[0])
    # intervals.sort(key=lambda x:x[0])
    end = sortedIntervals[0][1]
    res = 0
    for i in range(1, len(sortedIntervals)):
      interval = sortedIntervals[i]
      if end > interval[0]:
        res += 1
        end = min(end, interval[1])
      else:
        end = interval[1]
    return res
