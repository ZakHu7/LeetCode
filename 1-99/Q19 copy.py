# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    dummyHead = dummy
    runner = dummy
    for _ in range(n+1):
      runner = runner.next
    while runner:
      runner = runner.next
      dummyHead = dummyHead.next
    dummyHead.next = dummyHead.next.next
    return dummy.next

