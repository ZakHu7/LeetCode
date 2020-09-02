class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def getLinkedListLen(self, l):
        result = 0
        while l:
            l = l.next
            result += 1
        return result

    # Only called when len of l1 and l2 are same
    # return node and carry
    def addLinkedListR(self, l1, l2):
        if not l1 and not l2:
            return None, 0
        nextNode, carry = self.addLinkedListR(l1.next, l2.next)
        val = l1.val + l2.val + carry
        curNode = Node(val%10, nextNode)
        return curNode, val//10
    
    def addCarryR(self, l1, size, initialResult, carry):
        if size == 1:
            val = l1.val + carry
            result = Node(val%10, initialResult)
            return result, val//10
        result, newCarry = self.addCarryR(l1.next, size-1, initialResult, carry)
        val = l1.val + newCarry
        result = Node(val%10, result)
        return result, val//10



    def addLinkedList(self, l1, l2):
        len1 = self.getLinkedListLen(l1)
        len2 = self.getLinkedListLen(l2)
        
        diff = len1 - len2 #if positive, l1 is longer

        short = l2 if diff > 0 else l1
        long = l1 if diff > 0 else l2
        longCut = long

        for _ in range(abs(diff)):
            longCut = longCut.next
        

        result, carry = self.addLinkedListR(short, longCut)
        if abs(diff) != 0:
            result, newCarry = self.addCarryR(long, abs(diff), result, carry)
            if newCarry:
                result = Node(newCarry, result)

        return result

s = Solution()
l1 = Node(6, Node(1, Node(7, None)))
l2 = Node(2, Node(9, Node(5, Node(5, None))))

r = s.addLinkedList(l2,l1)

while r:
    print(r.val)
    r = r.next
    