# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(0)
        dummy.next = head
        while head and head.next:
          if head.val == head.next.val:
            while head.next and head.val == head.next.val:
              head = head.next
            head = head.next
            prev.next = head
          else:
            prev = prev.next
            head = head.next
        return dummy.next

        
        # head = self.deleteDuplicatesFront(head)
        # self.deleteDuplicatesMiddle(head)
        # return head
    # def deleteDuplicatesFront(self, head):
    #   while head:
    #     isDup = False
    #     while head.next and head.next.val == head.val:
    #       head.next = head.next.next
    #       isDup = True
    #     if isDup:
    #       head = head.next
    #     else:
    #       return head
    #   return head
    # def deleteDuplicatesMiddle(self, head):
    #   while head and head.next:
    #     isDup = False
    #     while head.next and head.next.next and head.next.val == head.next.next.val:
    #       head.next = head.next.next
    #       isDup = True
    #     if isDup:
    #       head.next = head.next.next
    #     else:
    #       head = head.next



# 1->2->3->3->4->4->5
# 1->1->1->2->3

a = ListNode(0)
pre = a
b = ListNode(2, ListNode(3, ListNode(4)))
a.next = b
print(a.next.val)
print(b.val)
b = b.next
pre.next = b
print(a.next.val)
print(b.val)
b = b.next
pre.next = b
print(a.next.val)
print(b.val)
