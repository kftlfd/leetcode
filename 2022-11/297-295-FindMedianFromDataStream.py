"""
Leetcode
295. Find Median from Data Stream (hard)
2022-11-12

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

 - For example, for arr = [2,3,4], the median is 3.
 - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

 - MedianFinder() initializes the MedianFinder object.
 - void addNum(int num) adds the integer num from the data stream to the data structure.
 - double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# from sortedcontainers import SortedList
from typing import List, Optional
from heapq import heappush, heappop


# wrong
class MedianFinder:

    def __init__(self):
        self.stack = []
        self.len = 0

    def addNum(self, num: int) -> None:
        heappush(self.stack, num)
        self.stack.append(num)
        self.len += 1

    def findMedian(self) -> float:
        if self.len % 2 == 0:
            a = (self.len - 1) // 2
            b = (self.len + 1) // 2
            return (self.stack[a] + self.stack[b]) / 2
        else:
            return self.stack[self.len // 2]


# https://leetcode.com/problems/find-median-from-data-stream/discuss/2805054/python3-Max-and-Min-heaps-oror-SortedList-oror-O(log-n)
# Runtime: 1788 ms, faster than 17.15% of Python3 online submissions for Find Median from Data Stream.
# Memory Usage: 36.1 MB, less than 57.44% of Python3 online submissions for Find Median from Data Stream.
class MedianFinder1:

    def __init__(self):
        self.s = SortedList()

    def addNum(self, num: int) -> None:
        self.s.add(num)

    def findMedian(self) -> float:
        l = len(self.s)
        if l % 2 == 0:
            return (self.s[l//2-1]+self.s[l//2])/2
        return self.s[l//2]


# https://leetcode.com/problems/find-median-from-data-stream/discuss/2805054/python3-Max-and-Min-heaps-oror-SortedList-oror-O(log-n)
# Runtime: 1550 ms, faster than 26.10% of Python3 online submissions for Find Median from Data Stream.
# Memory Usage: 35.8 MB, less than 80.22% of Python3 online submissions for Find Median from Data Stream.
class MedianFinder2:

    def __init__(self):
        # max heap to store the first half of the list
        self.maxHeap = []
        # min heap to store the second half of the list
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # push num into the correct heap
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        # banance the two heaps so that each of them representing half of the list
        # for odd length list, len(maxHeap) == len(minHeap)+1
        # for even length list, len(maxHeap) == len(minHeap)
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap)+1:
            heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self) -> float:
        # if the length of entire list is even,
        # get the mean of the two middle values
        if (len(self.maxHeap)+len(self.minHeap)) % 2 == 0:
            return (-self.maxHeap[0]+self.minHeap[0])/2

        # when odd, we know that the median is in maxHeap
        return -self.maxHeap[0]


s = MedianFinder2
tests = [
    (
        (
            ["MedianFinder", "addNum", "addNum",
                "findMedian", "addNum", "findMedian"],
            [[], [1], [2], [], [3], []]
        ),
        [None, None, None, 1.50000, None, 2.00000]
    ),

    (
        (
            ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
             "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0],
             [], [6], [], [3], [], [1], [], [0], [], [0], []]
        ),
        [None, None, 6.00000, None, 8.00000, None, 6.00000, None, 6.00000, None, 6.00000, None,
         5.50000, None, 6.00000, None, 5.50000, None, 5.00000, None, 4.00000, None, 3.00000]
    )
]
for inp, exp in tests:
    solution = None
    res = []
    for command, arg in zip(inp[0], inp[1]):
        if command == "MedianFinder":
            solution = s()
            res.append(None)
        elif command == "addNum":
            res.append(solution.addNum(*arg))
        elif command == "findMedian":
            res.append(solution.findMedian())
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
