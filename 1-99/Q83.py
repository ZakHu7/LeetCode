# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ret = head
        while head and head.next:
          while head.next and head.val == head.next.val:
            head.next = head.next.next
          head = head.next
        return ret

s = Solution()
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
s.deleteDuplicates(head)

while head:
  print(head.val)
  head = head.next