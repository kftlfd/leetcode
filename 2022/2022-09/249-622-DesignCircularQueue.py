"""
Leetcode
622. Design Circular Queue (medium)
2022-09-25

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

 - MyCircularQueue(k) Initializes the object with the size of the queue to be k.
 - int Front() Gets the front item from the queue. If the queue is empty, return -1.
 - int Rear() Gets the last item from the queue. If the queue is empty, return -1.
 - boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
 - boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
 - boolean isEmpty() Checks whether the circular queue is empty or not.
 - boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]
Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
"""


# https://leetcode.com/problems/design-circular-queue/discuss/172230/Python3-with-a-single-list-beats-100
# Runtime: 119 ms, faster than 47.22% of Python3 online submissions for Design Circular Queue.
# Memory Usage: 14.4 MB, less than 98.10% of Python3 online submissions for Design Circular Queue.
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.t = [0]*k
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        else:
            if self.rear == -1:
                self.rear = self.front = 0
            else:
                self.rear = (self.rear + 1) % self.max_size
            self.t[self.rear] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.t[self.front] if self.size != 0 else -1

    def Rear(self) -> int:
        return self.t[self.rear] if self.size != 0 else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
