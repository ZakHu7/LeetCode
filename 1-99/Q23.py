import heapq
from typing import List
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:

    heap = []
    for i in range(len(lists)):
      l = lists[i]
      if l:
        heapq.heappush(heap, (l.val, i, l))
        l = l.next
        lists[i] = l

    res = ListNode(0, None)
    dummy = res
    while heap:
      nextNode = heapq.heappop(heap)
      l = lists[nextNode[1]]
      if l:
        heapq.heappush(heap, (l.val, nextNode[1], l))
        l = l.next
        lists[nextNode[1]] = l
      res.next = nextNode[2]
      res = res.next
  
    return dummy.next

