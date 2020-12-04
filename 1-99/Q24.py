# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        while head and head.next:
          tmp = head.next.next
          head.next.next = head
          prev.next = head.next
          head.next = tmp
          prev = head
          head = head.next
        return dummy.next