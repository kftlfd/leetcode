"""
Leetcode
1187. Make Array Strictly Increasing (hard)
2023-06-17

Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].

Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].

Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.

Constraints:

    1 <= arr1.length, arr2.length <= 2000
    0 <= arr1[i], arr2[i] <= 10^9
"""

from typing import List
from bisect import bisect_left, insort_left, bisect_right
from collections import defaultdict


class Solution:
    """Wrong"""

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(arr2)
        ops = 0

        for i in range(1, len(arr1)):
            if arr1[i] > arr1[i - 1]:
                continue

            j = bisect_left(arr2, arr1[i - 1] + 1)
            if j >= len(arr2) or arr2[j] <= arr1[i]:
                return -1

            tmp = arr1[i]
            arr1[i] = arr2[j]
            arr2.pop(j)
            insort_left(arr2, tmp)
            ops += 1

        return ops


class Solution1:
    """
    leetcode solution 1: Top-down dynamic programming
    Runtime: 990 ms, faster than 35.39% of Python3 online submissions for Make Array Strictly Increasing.
    Memory Usage: 152.5 MB, less than 23.85% of Python3 online submissions for Make Array Strictly Increasing.
    """

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {}
        arr2 = sorted(arr2)

        def dfs(i, prev):
            if i == len(arr1):
                return 0

            if (i, prev) in dp:
                return dp[(i, prev)]

            cost = float('inf')

            # if arr[i] is already greater then prev, we can leave it
            if arr1[i] > prev:
                cost = dfs(i + 1, arr1[i])

            # find replacement with the smallest value in arr2
            idx = bisect_right(arr2, prev)

            # replace arr1[i] with a cost of 1 operation
            if idx < len(arr2):
                cost = min(cost, 1 + dfs(i + 1, arr2[idx]))

            dp[(i, prev)] = cost
            return cost

        ans = dfs(0, -1)

        return ans if ans < float('inf') else -1


class Solution2:
    """
    leetcode solution 2: Bottom-up Dynamic Programming
    Runtime: 652 ms, faster than 80.77% of Python3 online submissions for Make Array Strictly Increasing.
    Memory Usage: 16.8 MB, less than 74.62% of Python3 online submissions for Make Array Strictly Increasing.
    """

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}
        arr2.sort()
        n = len(arr2)

        for i in range(len(arr1)):
            new_dp = defaultdict(lambda: float('inf'))
            for prev in dp:
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
                idx = bisect_right(arr2, prev)
                if idx < n:
                    new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])
            dp = new_dp

        return min(dp.values()) if dp else -1


s = Solution1()
tests = [
    (([1, 5, 3, 6, 7], [1, 3, 2, 4]),
     1),

    (([1, 5, 3, 6, 7], [4, 3, 1]),
     2),

    (([1, 5, 3, 6, 7], [1, 6, 3, 3]),
     -1),
]
for inp, exp in tests:
    res = s.makeArrayIncreasing(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
