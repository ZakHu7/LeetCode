# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      retval = ListNode() ##be before the actual start of the list
      runner = retval
      while l1 and l2:
        if l1.val <= l2.val:
          runner.next = l1
          l1 = l1.next
        else:
          runner.next = l2
          l2 = l2.next
        runner = runner.next

      ## probably want to copy by value? idk
      runner.next = l1 or l2
      
      return retval.next;

s = Solution()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(5, ListNode(5, ListNode(6)))

l3 = s.mergeTwoLists(l1,l2);

print("after merge")
while l3:
  print(l3.val)
  l3 = l3.next