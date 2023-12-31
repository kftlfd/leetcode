"""
Leetcode
1035. Uncrossed Lines (medium)
2023-05-11

You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

    nums1[i] == nums2[j], and
    the line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

Example 1:
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

Example 2:
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3

Example 3:
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: recursive DP
    Runtime: 467 ms, faster than 7.35% of Python3 online submissions for Uncrossed Lines.
    Memory Usage: 60.2 MB, less than 5.25% of Python3 online submissions for Uncrossed Lines.
    """

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        memo = {}

        def solve(i, j):
            if i <= 0 or j <= 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if nums1[i - 1] == nums2[j - 1]:
                memo[(i, j)] = 1 + solve(i - 1, j - 1)
            else:
                memo[(i, j)] = max(solve(i - 1, j), solve(i, j - 1))

            return memo[(i, j)]

        return solve(n1, n2)


class Solution2:
    """
    leetcode solution 2: iterative DP
    Runtime: 186 ms, faster than 77.17% of Python3 online submissions for Uncrossed Lines.
    Memory Usage: 16.7 MB, less than 29.13% of Python3 online submissions for Uncrossed Lines.
    """

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n1][n2]


class Solution3:
    """
    leetcode solution 3: space-optimized DP
    Runtime: 168 ms, faster than 90.55% of Python3 online submissions for Uncrossed Lines.
    Memory Usage: 16.4 MB, less than 39.63% of Python3 online submissions for Uncrossed Lines.
    """

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [0] * (n2 + 1)
        dpPrev = [0] * (n2 + 1)

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = 1 + dpPrev[j - 1]
                else:
                    dp[j] = max(dp[j - 1], dpPrev[j])
            dpPrev = dp[:]

        return dp[n2]


s = Solution1()
tests = [
    (([1, 4, 2], [1, 2, 4]),
     2),

    (([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]),
     3),

    (([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]),
     2),
]
for inp, exp in tests:
    res = s.maxUncrossedLines(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
