# Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        tail = None

        while head:
            tmp = head.next
            head.next = tail
            tail = head
            head = tmp

        return tail




def printList(head):
    a = []
    while head:
        a.append(head.val)
        head = head.next
    print(a)

s = Solution()

a1 = ListNode(5)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(1)
a5 = ListNode(4)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5


printList(a1)
r = s.reverseList(a1)
printList(r)
