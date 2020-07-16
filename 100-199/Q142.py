# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        visited = set()
        

        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None
        

s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = b

print(s.detectCycle(a).val)
