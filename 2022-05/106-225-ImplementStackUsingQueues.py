"""
Leetcode
225. Implement Stack using Queues (easy)
2022-05-05

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

 - void push(int x) Pushes element x to the top of the stack.
 - int pop() Removes the element on the top of the stack and returns it.
 - int top() Returns the element on the top of the stack.
 - boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

 - You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
 - Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

"""

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



# try 1
# Runtime: 48 ms, faster than 30.72% of Python3 online submissions for Implement Stack using Queues.
# Memory Usage: 14.1 MB, less than 27.76% of Python3 online submissions for Implement Stack using Queues.
class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack += [x]
        

    def pop(self) -> int:
        l = len(self.stack)
        out = self.stack[l - 1]
        del self.stack[l - 1]
        return out
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def empty(self) -> bool:
        return len(self.stack) < 1
        


# leetcode solution
# Runtime: 40 ms, faster than 53.23% of Python3 online submissions for Implement Stack using Queues.
# Memory Usage: 14 MB, less than 27.76% of Python3 online submissions for Implement Stack using Queues.
class MyStack2:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.stack_top = None
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.stack_top = x
        

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.stack_top = self.q1.pop(0)
            self.q2.append(self.stack_top)
        out = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1
        return out
        

    def top(self) -> int:
        return self.stack_top
        

    def empty(self) -> bool:
        return len(self.q1) < 1
        


# python cheating
# Runtime: 42 ms, faster than 47.17% of Python3 online submissions for Implement Stack using Queues.
# Memory Usage: 14 MB, less than 76.44% of Python3 online submissions for Implement Stack using Queues.
class MyStack3:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack



tests = [
    [["MyStack","push","push","top","pop","empty"],
     [[],[1],[2],[],[],[]]]
]
for t in tests:
    print(*t)
    
    out = []
    for i in range(len(t[0])):
        if t[0][i] == 'MyStack':
            ms = MyStack2()
            out.append(None)
        elif t[0][i] == 'push':
            ms.push(t[1][i])
            out.append(None)
        elif t[0][i] == 'pop':
            x = ms.pop()
            out.append(x)
        elif t[0][i] == 'top':
            x = ms.top()
            out.append(x)
        elif t[0][i] == 'empty':
            x = ms.empty()
            out.append(x)
    
    print(out)
    print()
