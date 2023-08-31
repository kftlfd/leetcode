"""
Leetcode
1326. Minimum Number of Taps to Open to Water a Garden (hard)
2023-08-31

There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

Example 1:

Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]

Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.

Constraints:

    1 <= n <= 10^4
    ranges.length == n + 1
    0 <= ranges[i] <= 100
"""

from typing import List


class Solution:
    """
    leetcode solution 1: DP
    Runtime: 449 ms, faster than 33.09% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
    Memory Usage: 16.5 MB, less than 88.33% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
    """

    def minTaps(self, n: int, ranges: List[int]) -> int:
        # min number of taps needed for each position
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i, r in enumerate(ranges):
            tap_start = max(0, i - r)
            tap_end = min(n, i + r)

            for j in range(tap_start, tap_end + 1):
                # update with the minimum number of taps
                dp[tap_end] = min(dp[tap_end], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1


class Solution1:
    """
    leetcode solution 2: Greedy
    Runtime: 126 ms, faster than 83.57% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
    Memory Usage: 16.9 MB, less than 46.90% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
    """

    def minTaps(self, n: int, ranges: List[int]) -> int:
        # maximum reach for each position
        max_reach = [0] * (n + 1)

        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)

            # update the maximum reach for the leftmost position
            max_reach[start] = max(max_reach[start], end)

        taps = 0
        cur_end = 0
        next_end = 0

        # iterate through garden
        for i in range(n + 1):
            if i > next_end:  # current position cannot be reached
                return -1

            if i > cur_end:
                taps += 1
                cur_end = next_end

            next_end = max(next_end, max_reach[i])

        return taps


s = Solution()
tests = [
    ((5, [3, 4, 1, 1, 0, 0]),
     1),

    ((3, [0, 0, 0, 0]),
     -1),
]
for inp, exp in tests:
    res = s.minTaps(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
