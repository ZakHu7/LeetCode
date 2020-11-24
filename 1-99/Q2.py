from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        length1, lastL1 = self.getLinkedListLen(l1)
        length2, lastL2 = self.getLinkedListLen(l2)
        diff = length1 - length2
        if diff > 0:
          self.padLinkedList(lastL2, diff)
        else:
          self.padLinkedList(lastL1, diff)

        res = self.addTwoNumbersH(l1, l2, 0)

        # res = None
        # carry = 0
        # while l1 is not None:
        #   total = l1.val + l2.val + carry
        #   carry = total//10
        #   digitToInsert = total%10
        #   res = ListNode(digitToInsert, res)
        #   l1 = l1.next
        #   l2 = l2.next
        # if carry == 1:
        #   res = ListNode(carry, res)
        
        return res

    def addTwoNumbersH(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
      if not l1:
        if carry:
          return ListNode(carry, None)
        return None
      total = l1.val + l2.val + carry
      carry = total//10
      digitToInsert = total%10
      res = self.addTwoNumbersH(l1.next, l2.next, carry)
      return ListNode(digitToInsert, res)


    def getLinkedListLen(self, l: ListNode):
      length = 1
      while l.next is not None:
        length += 1
        l = l.next
      return length, l
    
    def padLinkedList(self, last: ListNode, padding: int):
      for _ in range(abs(padding)):
        newLast = ListNode(0, None)
        last.next = newLast
        last = newLast

    def printLinkedList(self, l):
      while l is not None:
        print(l.val)
        l = l.next

s = Solution()
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
l3 = s.addTwoNumbers(l1, l2)
s.printLinkedList(l3)


