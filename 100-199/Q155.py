class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, x):
        self.stack.append(x)
        min = x
        if self.min and self.min[-1] < x:
            min = self.min[-1]
        self.min.append(min)

    def pop(self):
        x = self.stack[-1]
        del(self.stack[-1])
        del(self.min[-1])
        # self.stack.remove(x)
        return x

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

s = MinStack()
a = []

s.push(1)
s.push(2)
s.push(-3)
s.push(10)


a.append(s.top())
a.append(s.pop())
a.append(s.pop())

a.append(s.getMin())

print(a)
