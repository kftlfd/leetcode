"""
Leetcode
215. Kth Largest Element in an Array (medium)
2023-08-14

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104
"""

from typing import List
import bisect
import heapq
import random


class Solution:
    """
    Runtime: 2511 ms, faster than 5.01% of Python3 online submissions for Kth Largest Element in an Array.
    Memory Usage: 29.3 MB, less than 89.91% of Python3 online submissions for Kth Largest Element in an Array.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            idx = bisect.bisect_left(q, num)
            q.insert(idx, num)
        return q[-k]


class Solution1:
    """
    leetcode solution: min-heap
    Runtime: 453 ms, faster than 88.34% of Python3 online submissions for Kth Largest Element in an Array.
    Memory Usage: 29.3 MB, less than 89.91% of Python3 online submissions for Kth Largest Element in an Array.
    Time: O(n * log(k))
    Space: O(k)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


class Solution2:
    """
    leetcode solution: quickselect
    Time: O(n) average, O(n^2) worst case
    Space: O(n)
    Runtime: 432 ms, faster than 93.79% of Python3 online submissions for Kth Largest Element in an Array.
    Memory Usage: 30.7 MB, less than 19.88% of Python3 online submissions for Kth Largest Element in an Array.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left = []
            mid = []
            right = []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)

            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))

            return pivot

        return quick_select(nums, k)


class Solution3:
    """
    leetcode solution: counting sort
    Time: O(n + m) -- m = max(nums) - min(nums)
    Space: O(m)
    Runtime: 401 ms, faster than 99.38% of Python3 online submissions for Kth Largest Element in an Array.
    Memory Usage: 29.5 MB, less than 72.41% of Python3 online submissions for Kth Largest Element in an Array.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value

        return -1


s = Solution()
tests = [
    (([3, 2, 1, 5, 6, 4], 2),
     5),

    (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
     4)
]
for inp, exp in tests:
    res = s.findKthLargest(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
