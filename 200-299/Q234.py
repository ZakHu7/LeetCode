# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if not head:
            return True

        # O(n) time, O(1) space
        # Find length of list
        runner = head
        length = 0

        while runner:
            length += 1
            runner = runner.next

        if length % 2 == 0:
            skip = length // 2
        else:
            skip = length // 2 + 1

        reverseHead = head
        for i in range(skip):
            reverseHead = reverseHead.next

        reverseHead = self.reverse(reverseHead)
        for i in range(length - skip):
            if head.val != reverseHead.val:
                return False
            head = head.next
            reverseHead = reverseHead.next
        return True
    def reverse(self, head):
        prev = after = None
        while head:
            after = head.next
            head.next = prev
            prev = head
            head = after
        return prev            
            

        


s = Solution()

a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(2)
a4 = ListNode(1)

a1.next = a2
a2.next = a3
a3.next = a4


print(s.isPalindrome(a1))