"""
Leetcode
703. Kth Largest Element in a Stream (easy)
2022-04-08

Design a class to find the kth largest element in a stream. Note that 
it is the kth largest element in the sorted order, not the kth distinct 
element.

Implement KthLargest class:

 - KthLargest(int k, int[] nums) Initializes the object with the integer 
   k and the stream of integers nums.
 - int add(int val) Appends the integer val to the stream and returns the 
   element representing the kth largest element in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]
"""
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

from typing import List
import heapq



# https://leetcode.com/problems/kth-largest-element-in-a-stream/solution/1342101
# Runtime: 182 ms, faster than 26.48% of Python3 online submissions for Kth Largest Element in a Stream.
# Memory Usage: 18.5 MB, less than 10.77% of Python3 online submissions for Kth Largest Element in a Stream.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min-heap
        self.k = k
        self.heap = []
        n = len(nums)
        
        # Add all the elements upto k
        for i in range(min(n, k)):
            self.heap.append(nums[i])
            
        heapq.heapify(self.heap)
        
        # add remaining elements
        for i in range(k, n):
            self.add(nums[i])
        

    def add(self, val: int) -> int:
        # if heap doesn't have k elements yet, add val
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        
        # if the new val is larger than the current k-th element,
        # remove the k-th and add this to the heap
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        # k-th largest is the top of min-heap
        return self.heap[0]



tests = [
    [["KthLargest","add","add","add","add","add"],
     [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]]
]
for t in tests:
    print(t)

    kl = None
    out = []

    for i in range(len(t[0])):
        if t[0][i] == "KthLargest":
            kl = KthLargest(t[1][i][0], t[1][i][1])
            out.append(None)
        else:
            out.append(kl.add(t[1][i][0]))

    print(out)
    print()
