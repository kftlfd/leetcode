"""
Leetcode
2026-09-12
3414. Maximum Score of Non-overlapping Intervals
Hard

You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 

Example 1:

Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

Output: [2,3]

Explanation:

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

Example 2:

Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Output: [1,3,5,6]

Explanation:

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

 

Constraints:

    1 <= intevals.length <= 5 * 10^4
    intervals[i].length == 3
    intervals[i] = [li, ri, weighti]
    1 <= li <= ri <= 10^9
    1 <= weighti <= 10^9


Hint 1
Use Dynamic Programming.
Hint 2
Sort intervals by right boundary.
Hint 3
Let dp[r][i] denote the maximum score having picked r intervals from the prefix of intervals ending at index i.
Hint 4
dp[r][i] = max(dp[r][i - 1], intervals[i][2] + dp[r][j]) where j is the largest index such that intervals[j][1] < intervals[i][0].
Hint 5
Since intervals is sorted by right boundary, we can find index j using binary search.
"""

from bisect import bisect_left
from typing import List


class Solution:
    """
    leetcode solution: Dynamic Programming + Binary Search
    Runtime 1501ms Beats 59.32%
    Memory 82.68MB Beats 44.07%
    """

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [
            (intervals[i][1], intervals[i][0], intervals[i][2], i)
            for i in range(n)
        ]
        # Sort by right endpoint.
        arr.sort(key=lambda x: x[0])

        dp = [[0] * 5 for _ in range(n + 1)]
        indices = [[[] for _ in range(5)] for _ in range(n + 1)]

        for i in range(n):
            r, l, weight, idx = arr[i]
            # Use binary search to find intervals whose right endpoints are smaller than l.
            k = bisect_left(arr, (l,), hi=i)

            for j in range(1, 5):
                s1 = dp[i][j]
                s2 = dp[k][j - 1] + weight
                if s1 > s2:
                    dp[i + 1][j] = dp[i][j]
                    indices[i + 1][j] = indices[i][j].copy()
                    continue

                new_index = indices[k][j - 1].copy()
                new_index.append(idx)
                new_index.sort()
                if s1 == s2 and indices[i][j] < new_index:
                    new_index = indices[i][j].copy()
                dp[i + 1][j] = s2
                indices[i + 1][j] = new_index

        return indices[n][4]
