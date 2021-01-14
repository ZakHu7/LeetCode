from typing import List
class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda x:x[0])
    res = []
    [start, end] = intervals[0]
    for i in range(1, len(intervals)):
      interval = intervals[i]
      if end < interval[0]:
        res.append([start, end])
        [start, end] = interval
      else:
        end = max(end, interval[1])
    res.append([start, end])
    return res


s = Solution()
intervals = [[1,4],[4,5]]
print(s.merge(intervals))