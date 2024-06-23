"""
Leetcode
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium
2024-06-23

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= limit <= 10^9
"""

from collections import deque
from typing import List
import heapq
from sortedcontainers import SortedDict


class Solution:
    """
    Time Limit Exceeded
    """

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = [nums[0]]
        start = 0
        ans = 1

        for end in range(1, len(nums)):
            num = nums[end]
            heapq.heappush(window, num)
            w_min = heapq.nsmallest(1, window)[0]
            w_max = heapq.nlargest(1, window)[0]

            if abs(w_max - w_min) <= limit:
                ans = max(ans, end - start + 1)
            else:
                while start < end and abs(w_max - w_min) > limit:
                    window.remove(nums[start])
                    heapq.heapify(window)
                    w_min = heapq.nsmallest(1, window)[0]
                    w_max = heapq.nlargest(1, window)[0]
                    start += 1

        return ans


class Solution1:
    """
    leetcode solution 1: Two Heaps
    Runtime: 623 ms, faster than 21.48% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    Memory Usage: 36 MB, less than 10.55% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    """

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_heap = []
        min_heap = []

        left = 0
        max_length = 0

        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            # Check if the absolute difference between the maximum and minimum values in the current window exceeds the limit
            while -max_heap[0][0] - min_heap[0][0] > limit:
                # Move the left pointer to the right until the condition is satisfied.
                # This ensures we remove the element causing the violation
                left = min(max_heap[0][1], min_heap[0][1]) + 1

                # Remove elements from the heaps that are outside the current window
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            # Update max_length with the length of the current valid window
            max_length = max(max_length, right - left + 1)

        return max_length


class Solution2:
    """
    leetcode solution 2: Multiset
    Runtime: 1026 ms, faster than 7.93% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    Memory Usage: 26.2 MB, less than 68.67% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    """

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # SortedDict to maintain the elements within the current window
        window = SortedDict()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] in window:
                window[nums[right]] += 1
            else:
                window[nums[right]] = 1

            # Check if the absolute difference between the maximum and minimum values in the current window exceed the limit
            while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit:
                # Remove the element at the left pointer from the SortedDict
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    window.pop(nums[left])
                # Move the left pointer to the right to exclude the element causing the violation
                left += 1

            # Update maxLength with the length of the current valid window
            max_length = max(max_length, right - left + 1)

        return max_length


class Solution3:
    """
    leetcode solution 3: Two Deques
    Runtime: 441 ms, faster than 70.46% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    Memory Usage: 25.9 MB, less than 78.52% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    """

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Maintain the max_deque in decreasing order
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            # Maintain the min_deque in increasing order
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            # Check if the current window exceeds the limit
            while max_deque[0] - min_deque[0] > limit:
                # Remove the elements that are out of the current window
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


s = Solution()
tests = [
    (([4, 2, 2, 2, 4, 4, 2, 2], 0),
     3),
]
for inp, exp in tests:
    res = s.longestSubarray(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
