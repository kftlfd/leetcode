"""
Leetcode
2024-12-14
2762. Continuous Subarrays
Medium

You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

    Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.

Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [5,4,2,4]
Output: 8
Explanation: 
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
Thereare no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.

 

Example 2:

Input: nums = [1,2,3]
Output: 6
Explanation: 
Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9

Hints:
- Try using the sliding window technique.
- Use a set or map to keep track of the maximum and minimum of subarrays.
"""

from collections import deque
import heapq
from typing import List


class Solution:
    """
    leetcode solution 1: Sorted Map
    Runtime: 705 ms, faster than 48.80% of Python3 online submissions for Continuous Subarrays.
    Memory Usage: 27.6 MB, less than 28.65% of Python3 online submissions for Continuous Subarrays.
    """

    def continuousSubarrays(self, nums: List[int]) -> int:
        # Map to maintain sorted frequency map of current window
        freq = {}
        left = right = 0
        count = 0  # Total count of valid subarrays

        while right < len(nums):
            # Add current element to frequency map
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # While window violates the condition |nums[i] - nums[j]| ≤ 2
            # Shrink window from left
            while max(freq) - min(freq) > 2:
                # Remove leftmost element from frequency map
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # Add count of all valid subarrays ending at right
            count += right - left + 1
            right += 1

        return count


class Solution2:
    """
    leetcode solution 2: Priority Queue
    Runtime: 797 ms, faster than 25.00% of Python3 online submissions for Continuous Subarrays.
    Memory Usage: 44.4 MB, less than 10.03% of Python3 online submissions for Continuous Subarrays.
    """

    def continuousSubarrays(self, nums: List[int]) -> int:
        # Two heaps to track min/max indices, sorted by nums[index]
        min_heap = []  # (nums[i], i) tuples for min tracking
        max_heap = []  # (-nums[i], i) tuples for max tracking
        left = right = 0
        count = 0

        while right < len(nums):
            # Add current index to both heaps
            # For max heap, negate value to convert min heap to max heap
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))

            # While window violates |nums[i] - nums[j]| ≤ 2
            # Shrink window from left and remove outdated indices
            while left < right and -max_heap[0][0] - min_heap[0][0] > 2:
                left += 1

                # Remove indices outside window from both heaps
                while min_heap and min_heap[0][1] < left:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1] < left:
                    heapq.heappop(max_heap)

            count += right - left + 1
            right += 1

        return count


class Solution3:
    """
    leetcode solution 3: Monotonic Deque
    Runtime: 626 ms, faster than 66.87% of Python3 online submissions for Continuous Subarrays.
    Memory Usage: 27.9 MB, less than 16.33% of Python3 online submissions for Continuous Subarrays.
    """

    def continuousSubarrays(self, nums: List[int]) -> int:
        # Monotonic deque to track maximum and minimum elements
        max_q = deque()
        min_q = deque()
        left = 0
        count = 0

        for right, num in enumerate(nums):
            # Maintain decreasing monotonic deque for maximum values
            while max_q and nums[max_q[-1]] < num:
                max_q.pop()
            max_q.append(right)

            # Maintain increasing monotonic deque for minimum values
            while min_q and nums[min_q[-1]] > num:
                min_q.pop()
            min_q.append(right)

            # Shrink window if max-min difference exceeds 2
            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > 2:
                # Move left pointer past the element that breaks the condition
                if max_q[0] < min_q[0]:
                    left = max_q[0] + 1
                    max_q.popleft()
                else:
                    left = min_q[0] + 1
                    min_q.popleft()

            # Add count of all valid subarrays ending at current right pointer
            count += right - left + 1

        return count


class Solution4:
    """
    leetcode solution 4: Optimized Two Pointer
    Runtime: 614 ms, faster than 75.90% of Python3 online submissions for Continuous Subarrays.
    Memory Usage: 27.3 MB, less than 49.00% of Python3 online submissions for Continuous Subarrays.
    """

    def continuousSubarrays(self, nums: List[int]) -> int:
        right = left = 0
        window_len = total = 0

        # Initialize window with first element
        cur_min = cur_max = nums[right]

        for right, num_right in enumerate(nums):
            # Update min and max for current window
            cur_min = min(cur_min, num_right)
            cur_max = max(cur_max, num_right)

            # If window condition breaks (diff > 2)
            if cur_max - cur_min > 2:
                # Add subarrays from previous valid window
                window_len = right - left
                total += window_len * (window_len + 1) // 2

                # Start new window at current position
                left = right
                cur_min = cur_max = num_right

                # Expand left boundary while maintaining condition
                while left > 0 and abs(num_right - nums[left - 1]) <= 2:
                    left -= 1
                    cur_min = min(cur_min, nums[left])
                    cur_max = max(cur_max, nums[left])

                # Remove overcounted subarrays if left boundary expanded
                if left < right:
                    window_len = right - left
                    total -= window_len * (window_len + 1) // 2

        # Add subarrays from final window
        window_len = right - left + 1
        total += window_len * (window_len + 1) // 2

        return total
