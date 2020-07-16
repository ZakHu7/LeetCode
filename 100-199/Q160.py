# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLength(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l
    def getIntersectionNode(self, headA, headB):
        # get length, then make both same length

        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)

        while lengthA < lengthB:
            lengthB -= 1
            headB = headB.next
        while lengthA > lengthB:
            lengthA -= 1
            headA = headA.next
        
        while headA and headB:
            if headA == headB:
                return headA.val
            headA = headA.next
            headB = headB.next
        
        return None

s = Solution()

c1 = ListNode(4)
c2 = ListNode(0)

a1 = ListNode(5)
a2 = ListNode(1)
a3 = ListNode(6)

b1 = ListNode(8)

a1.next = a2
a2.next = a3
a3.next = c1
c1.next = c2
b1.next = c1

print(s.getIntersectionNode(b1, a1))

        