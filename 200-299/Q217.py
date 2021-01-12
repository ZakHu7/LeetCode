from typing import List
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    d = set()
    for n in nums:
      if n in d:
        return True
      d.add(n)
    return False