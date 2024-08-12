"""
Leetcode
703. Kth Largest Element in a Stream
Easy
2024-08-12

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

 

Constraints:

    1 <= k <= 10^4
    0 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    -10^4 <= val <= 10^4
    At most 10^4 calls will be made to add.
    It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import bisect
import heapq
from typing import List


class KthLargest:
    """
    Runtime: 105 ms, faster than 12.59% of Python3 online submissions for Kth Largest Element in a Stream.
    Memory Usage: 21 MB, less than 7.95% of Python3 online submissions for Kth Largest Element in a Stream.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        self.nums.insert(bisect.bisect(self.nums, val), val)
        return self.nums[-self.k]


class KthLargest2:
    """
    leetcode solution 2: Heap
    Runtime: 77 ms, faster than 70.46% of Python3 online submissions for Kth Largest Element in a Stream.
    Memory Usage: 20.5 MB, less than 73.34% of Python3 online submissions for Kth Largest Element in a Stream.
    """

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add to our min_heap if we haven't processed k elements yet
        # or if val is greater than the top element (the k-th largest)
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]
