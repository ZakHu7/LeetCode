from typing import List
class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(intervals) == 0:
      return [newInterval]
    left, right = [], []
    mergedInterval = newInterval
    for interval in intervals:
      if interval[1] < newInterval[0]:
        left.append(interval)
      if interval[0] > newInterval[1]:
        right.append(interval)
    if len(left) <= len(intervals)-1 and len(right) <= len(intervals)-1:
      mergedInterval = [min(newInterval[0], intervals[(len(left))][0]),
                        max(newInterval[1], intervals[-len(right)-1][1])]
    return left + [mergedInterval] + right

s = Solution()
intervals = [[1,5]]
newInterval = [-3,0]
print(s.insert(intervals, newInterval))