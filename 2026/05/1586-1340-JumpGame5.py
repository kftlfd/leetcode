"""
Leetcode
2026-05-24
1340. Jump Game V
Hard

Given an array of integers arr and an integer d. In one step you can jump from index i to index:

    i + x where: i + x < arr.length and  0 < x <= d.
    i - x where: i - x >= 0 and  0 < x <= d.

In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.

Example 2:

Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.

Example 3:

Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies. 

 

Constraints:

    1 <= arr.length <= 1000
    1 <= arr[i] <= 10^5
    1 <= d <= arr.length


"""

from typing import List


class Solution:
    """
    Runtime 100ms Beats 94.00%
    Memory 19.49MB Beats 89.43%
    """

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n

        for h, i in sorted((h, i) for i, h in enumerate(arr)):
            nxt = 0
            for idx in range(i - 1, max(0, i - d) - 1, -1):
                if arr[idx] >= h:
                    break
                nxt = max(nxt, dp[idx])
            for idx in range(i + 1, min(n, i + d + 1)):
                if arr[idx] >= h:
                    break
                nxt = max(nxt, dp[idx])
            dp[i] += nxt

        return max(dp)


class Solution1:
    """
    leetcode solution: Memoization Search
    Runtime 373ms Beats 7.72%
    Memory 24.05MB Beats 36.57%
    """

    def maxJumps(self, arr: List[int], d: int) -> int:
        seen = {}

        def dfs(pos):
            if pos in seen:
                return
            seen[pos] = 1

            i = pos - 1
            while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i -= 1
            i = pos + 1
            while i < len(arr) and i - pos <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i += 1

        for i in range(len(arr)):
            dfs(i)

        return max(seen.values())
