"""
Leetcode
2024-11-17
862. Shortest Subarray with Sum at Least K
Hard

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1

Example 2:

Input: nums = [1,2], k = 4
Output: -1

Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3

 

Constraints:

    1 <= nums.length <= 10^5
    -10^5 <= nums[i] <= 10^5
    1 <= k <= 10^9
"""

from collections import deque
from heapq import heappop, heappush
from typing import List, Tuple


class Solution:
    """
    Wrong Answer
    """

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        left = 0
        window_sum = 0
        negatives = 0
        ans = len(nums) + 1

        for right, num in enumerate(nums):
            window_sum += num
            negatives += min(num, 0)
            while window_sum - negatives >= k:
                if window_sum >= k:
                    ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                negatives += min(nums[left], 0)
                if left >= right:
                    break
                left += 1

        return ans if ans < len(nums) + 1 else -1


class Solution1:
    """
    leetcode solution 1: Priority Queue
    Runtime: 406 ms, faster than 14.53% of Python3 online submissions for Shortest Subarray with Sum at Least K.
    Memory Usage: 37 MB, less than 8.07% of Python3 online submissions for Shortest Subarray with Sum at Least K.
    """

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Initialize result to the maximum possible integer value
        shortest_subarray_length = float("inf")

        cumulative_sum = 0

        # Min-heap to store cumulative sum and its corresponding index
        prefix_sum_heap = []

        # Iterate through the array
        for i, num in enumerate(nums):
            # Update cumulative sum
            cumulative_sum += num

            # If cumulative sum is already >= k, update shortest length
            if cumulative_sum >= k:
                shortest_subarray_length = min(shortest_subarray_length, i + 1)

            # Remove subarrays from heap that can form a valid subarray
            while (
                prefix_sum_heap and cumulative_sum - prefix_sum_heap[0][0] >= k
            ):
                # Update shortest subarray length
                shortest_subarray_length = min(
                    shortest_subarray_length, i - heappop(prefix_sum_heap)[1]
                )

            # Add current cumulative sum and index to heap
            heappush(prefix_sum_heap, (cumulative_sum, i))

        # Return -1 if no valid subarray found
        return (
            -1
            if shortest_subarray_length == float("inf")
            else shortest_subarray_length
        )


class Solution2:
    """
    leetcode solution 2: Monotonic Stack + Binary Search
    Runtime: 907 ms, faster than 5.09% of Python3 online submissions for Shortest Subarray with Sum at Least K.
    Memory Usage: 41.6 MB, less than 5.22% of Python3 online submissions for Shortest Subarray with Sum at Least K.
    """

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Stack-like list to store cumulative sums and their indices
        cumulative_sum_stack = [(0, -1)]

        running_cumulative_sum = 0
        shortest_subarray_length = float("inf")

        for i in range(n):
            # Update cumulative sum
            running_cumulative_sum += nums[i]

            # Remove entries from stack that are larger than current cumulative sum
            while (
                cumulative_sum_stack
                and running_cumulative_sum <= cumulative_sum_stack[-1][0]
            ):
                cumulative_sum_stack.pop()

            # Add current cumulative sum and index to stack
            cumulative_sum_stack.append((running_cumulative_sum, i))

            candidate_index = self._find_candidate_index(
                cumulative_sum_stack, running_cumulative_sum - k
            )

            # If a valid candidate is found, update the shortest subarray length
            if candidate_index != -1:
                shortest_subarray_length = min(
                    shortest_subarray_length,
                    i - cumulative_sum_stack[candidate_index][1],
                )

        # Return -1 if no valid subarray found
        return (
            shortest_subarray_length
            if shortest_subarray_length != float("inf")
            else -1
        )

    # Binary search to find the largest index where cumulative sum is <= target
    def _find_candidate_index(
        self, nums: List[Tuple[int, int]], target: int
    ) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right


class Solution3:
    """
    leetcode solution 3: Deque
    Runtime: 196 ms, faster than 59.08% of Python3 online submissions for Shortest Subarray with Sum at Least K.
    Memory Usage: 33.1 MB, less than 28.82% of Python3 online submissions for Shortest Subarray with Sum at Least K.
    """

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Size is n+1 to handle subarrays starting from index 0
        prefix_sums = [0] * (n + 1)

        # Calculate prefix sums
        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        candidate_indices = deque()

        shortest_subarray_length = float("inf")

        for i in range(n + 1):
            # Remove candidates from front of deque where subarray sum meets target
            while (
                candidate_indices
                and prefix_sums[i] - prefix_sums[candidate_indices[0]]
                >= k
            ):
                # Update shortest subarray length
                shortest_subarray_length = min(
                    shortest_subarray_length, i - candidate_indices.popleft()
                )

            # Maintain monotonicity by removing indices with larger prefix sums
            while (
                candidate_indices
                and prefix_sums[i] <= prefix_sums[candidate_indices[-1]]
            ):
                candidate_indices.pop()

            # Add current index to candidates
            candidate_indices.append(i)

        # Return -1 if no valid subarray found
        return (
            shortest_subarray_length
            if shortest_subarray_length != float("inf")
            else -1
        )


s = Solution()
tests = [
    (([31, 63, -38, 43, 65, 74, 90, -23, 45, 22], 341),
     9),

    (([1], 1),
     1),

    (([18, 83, -43, -18, 60], 18),
     1),

    (([84, -37, 32, 40, 95], 167),
     3),
]
for inp, exp in tests:
    res = s.shortestSubarray(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
