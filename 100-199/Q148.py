# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def printList(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        print(a)

    def findLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def merge(self, left, right):
        head = left
        leftParent = None
        while left and right:
            if left.val < right.val:
                leftParent = left
                left = left.next

            else:

                tmpRight = right
                right = right.next
                if leftParent:
                    leftParent.next = tmpRight
                else:
                    head = tmpRight
                leftParent = tmpRight
                leftParent.next = left


        if not left:
            leftParent.next = right
        
        return head


    def sortListR(self, head, length):
        if length == 0 or length == 1:
            return head

        halfLength = length // 2

        headCopy = head
        rightListHead = headCopy
        for i in range(halfLength):
            rightListHead = rightListHead.next

        leftListHead = headCopy
        for i in range(halfLength - 1):
            leftListHead = leftListHead.next
        leftListHead.next = None


        leftList = self.sortListR(head, halfLength)
        rightList = self.sortListR(rightListHead, length - halfLength)

        # self.printList(leftList)
        # self.printList(rightList)

        sortedHead = self.merge(leftList, rightList)
        return sortedHead

    def sortList(self, head):
        length = self.findLength(head)
        return self.sortListR(head, length)
    

s = Solution()

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)

a4.next = a2
a2.next = a1
a1.next = a3

# head = s.sortList(a4)

b1 = ListNode(-1)
b2 = ListNode(4)
b3 = ListNode(0)
b4 = ListNode(3)
b5 = ListNode(2)

b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5
s.printList(b1)

head2 = s.sortList(b1)

# s.printList(head)

s.printList(head2)
s.printList(b1)
# s.printList(a4)
