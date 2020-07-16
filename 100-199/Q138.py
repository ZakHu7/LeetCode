"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next = None, random = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        dic = {}
        headCopy = head
        while headCopy:
            dic[headCopy] = Node(headCopy.val)
            headCopy = headCopy.next

        headCopy = head
        while headCopy:
            dic[headCopy].next = dic[headCopy.next] if headCopy.next else None
            dic[headCopy].random = dic[headCopy.random] if headCopy.random else None
            headCopy = headCopy.next

        return dic[head] if head else None


s = Solution()

a0 = None

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
        
a1.next = a2
a2.next = a3
a3.next = a4

a1.random = a3
a2.random = None
a3.random = a2
a4.random = a3

b = s.copyRandomList(a0)

while b:
    print("VAL: " + str(b.val))
    print("NEXT: " + str(b.next.val if b.next else None))
    print("RANDOM: " + str(b.random.val if b.random else None))
    b = b.next

