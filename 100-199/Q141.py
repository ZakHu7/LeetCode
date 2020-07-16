# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while slow and fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = c

print(s.hasCycle(a))
        