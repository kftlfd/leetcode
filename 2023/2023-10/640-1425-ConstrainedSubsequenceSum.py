"""
Leetcode
1425. Constrained Subsequence Sum (hard)
2023-10-21

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].

Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.

Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].

 

Constraints:

    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""

from typing import List
import heapq
from collections import deque
from sortedcontainers import SortedList


class Solution1:
    """
    leetcode solution 1: heap/priority queue
    Time: O(n * log(n))
    Space: O(n)
    Runtime: 1670 ms, faster than 31.92% of Python3 online submissions for Constrained Subsequence Sum.
    Memory Usage: 36.4 MB, less than 17.87% of Python3 online submissions for Constrained Subsequence Sum.
    """

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]

        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)

            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heapq.heappush(heap, (-curr, i))

        return ans


class Solution2:
    """
    leetcode solution 2: TreeMap-Like Data Structure
    Time: O(n * log(k))
    Space: O(n)
    Runtime: 2258 ms, faster than 8.09% of Python3 online submissions for Constrained Subsequence Sum.
    Memory Usage: 31.2 MB, less than 31.06% of Python3 online submissions for Constrained Subsequence Sum.
    """

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        window = SortedList([0])
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = nums[i] + window[-1]
            window.add(dp[i])
            if i >= k:
                window.remove(dp[i - k])

        return max(dp)


class Solution3:
    """
    leetcode solution 3: Monotonic Deque
    Time: O(n)
    Space: O(n)
    Runtime: 1264 ms, faster than 94.89% of Python3 online submissions for Constrained Subsequence Sum.
    Memory Usage: 30 MB, less than 69.79% of Python3 online submissions for Constrained Subsequence Sum.
    """

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if queue and i - queue[0] > k:
                queue.popleft()

            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()

            if dp[i] > 0:
                queue.append(i)

        return max(dp)
