"""
Leetcode
225. Implement Stack using Queues (easy)
2023-08-28

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

    You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:

    1 <= x <= 9
    At most 100 calls will be made to push, pop, top, and empty.
    All the calls to pop and top are valid.
"""

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyStack:
    """
    leetcode solution
    Runtime: 39 ms, faster than 66.93% of Python3 online submissions for Implement Stack using Queues.
    Memory Usage: 16.4 MB, less than 31.94% of Python3 online submissions for Implement Stack using Queues.
    """

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
