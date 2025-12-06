"""
Leetcode
2025-12-06
3578. Count Partitions With Max-Min Difference at Most K
Medium

You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

    [[9], [4], [1], [3], [7]]
    [[9], [4], [1], [3, 7]]
    [[9], [4], [1, 3], [7]]
    [[9], [4, 1], [3], [7]]
    [[9], [4, 1], [3, 7]]
    [[9], [4, 1, 3], [7]]

Example 2:

Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

    [[3], [3], [4]]
    [[3, 3], [4]]

 

Constraints:

    2 <= nums.length <= 5 * 10^4
    1 <= nums[i] <= 10^9
    0 <= k <= 10^9


Hint 1
Use dynamic programming.
Hint 2
Let dp[idx] be the count of ways to partition the array with the last partition ending at index idx.
Hint 3
Try using a sliding window; we can track the minimum and maximum in the window using deques.
"""

from collections import deque
from typing import List

from sortedcontainers import SortedList


class Solution1:
    """
    leetcode solution 1: Sliding Window + Dynamic Programming
    Runtime 1491ms Beats 9.37%
    Memory 26.45MB Beats 42.71%
    """

    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        cnt = SortedList()

        dp[0] = 1
        prefix[0] = 1

        j = 0
        for i in range(n):
            cnt.add(nums[i])
            # adjust window
            while j <= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])
                j += 1
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod

        return dp[n]


class Solution2:
    """
    leetcode solution 2: Monotonic Queue Optimization
    Runtime 479ms Beats 46.87%
    Memory 27.12MB Beats 21.88%
    """

    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        min_q = deque()
        max_q = deque()

        dp[0] = 1
        prefix[0] = 1
        j = 0

        for i in range(n):
            # maintain the maximum value queue
            while max_q and nums[max_q[-1]] <= nums[i]:
                max_q.pop()
            max_q.append(i)

            # maintain the minimum value queue
            while min_q and nums[min_q[-1]] >= nums[i]:
                min_q.pop()
            min_q.append(i)

            # adjust window
            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == j:
                    max_q.popleft()
                if min_q[0] == j:
                    min_q.popleft()
                j += 1

            if j > 0:
                dp[i + 1] = (prefix[i] - prefix[j - 1] + mod) % mod
            else:
                dp[i + 1] = prefix[i] % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod

        return dp[n]
