from collections import deque
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head:
      return
    stack = deque()
    count = 0
    headCopy = head
    while headCopy:
      stack.append(headCopy)
      headCopy = headCopy.next
      count += 1
    middle = count//2

    for _ in range(middle):
      tmp = head.next
      head.next = stack.pop()
      head.next.next = tmp
      head = tmp
    head.next = None