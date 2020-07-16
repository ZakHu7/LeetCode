
## doubly linked list to act like a queue, which also allows for easy removal of node in the middle
class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
###############################

class LRUCache:

    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        # print(self.tail.val)
    
    def removeNode(self, node):
        tmpPrev = node.prev
        node.prev.next = node.next
        node.next.prev = tmpPrev
    
    def popTail(self):
        popped = self.tail.prev
        popped.prev.next = self.tail
        self.tail.prev = popped.prev
        return popped



    def __init__(self, capacity):
        self.head = DLLNode(0, 0)
        self.tail = DLLNode(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.dict = {}
        self.capacity = capacity
        

    def get(self, key):
        if key in self.dict:
            node = self.dict.get(key)
            self.removeNode(node)
            self.addToHead(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.dict:    ## update if key is in dict
            self.removeNode(self.dict[key])
        elif self.capacity == 0:    ## if capacity is full, kick out lru
            lru = self.popTail()
            self.dict.pop(lru.key)
            # self.dict[key] = DLLNode(key, value)
            # head.addToHead(self.dict[key])
        else:
            self.capacity -= 1

        self.dict[key] = DLLNode(key, value)
        self.addToHead(self.dict[key])


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(3)
a = []

cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
a.append(cache.get(4))
a.append(cache.get(3))
a.append(cache.get(2))
a.append(cache.get(1))

cache.put(5,5)
a.append(cache.get(1))
a.append(cache.get(2))
a.append(cache.get(3))
a.append(cache.get(4))
a.append(cache.get(5))



print(a)
# print(a, a2)

