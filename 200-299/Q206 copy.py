# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#   def reverseList(self, head: ListNode) -> ListNode:
#     def reverseListH(head, newList):
#       if not head:
#         return newList
#       return reverseListH(head.next, ListNode(head.val, newList))

#     return reverseListH(head, None)
class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    newList = None
    while head:
      nextNode = head.next
      head.next = newList
      newList = head
      head = nextNode
    return newList