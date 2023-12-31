"""
Leetcode
1420. Build Array Where You Can Find The Maximum Exactly K Comparisons (hard)
2023-10-07

You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:

maximum_value = -1
maximum_index = -1
search_cost = 0
n = arr.length
for (i = 0; i < n; i++) {
    if (maximum_value < arr[i]) {
        maximum_value = arr[i]
        maximum_index = i
        search_cost += 1
    }
}
return maximum_index

You should build the array arr which has the following properties:

    arr has exactly n integers.
    1 <= arr[i] <= m where (0 <= i < n).
    After applying the mentioned algorithm to arr, the value search_cost is equal to k.

Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

 

Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.

Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

 

Constraints:

    1 <= n <= 50
    1 <= m <= 100
    0 <= k <= n
"""


from functools import cache


class Solution:
    """
    leetcode solution 1: Top-Down Dynamic Programming
    Time: O(n * m^2 * k)
    Space: O(n * m * k)
    Runtime: 798 ms, faster than 69.52% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    Memory Usage: 43.5 MB, less than 6.67% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    """

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(i, maxSoFar, remain):
            if i == n:
                return 1 if remain == 0 else 0

            ans = (maxSoFar * dp(i + 1, maxSoFar, remain)) % MOD

            for num in range(maxSoFar + 1, m + 1):
                ans = (ans + dp(i + 1, num, remain - 1)) % MOD

            return ans

        return dp(0, 0, k)


class Solution1:
    """
    leetcode solution 2: Bottom-Up Dynamic Programming
    Time: O(n * m^2 * k)
    Space: O(n * m * k)
    Runtime: 1062 ms, faster than 34.28% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    Memory Usage: 20.3 MB, less than 77.14% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    """

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        for num in range(len(dp[0])):
            dp[n][num][0] = 1

        for i in range(n - 1, -1, -1):
            for maxSoFar in range(m, -1, -1):
                for remain in range(k + 1):
                    ans = (maxSoFar * dp[i + 1][maxSoFar][remain]) % MOD

                    if remain > 0:
                        for num in range(maxSoFar + 1, m + 1):
                            ans = (ans + dp[i + 1][num][remain - 1]) % MOD

                    dp[i][maxSoFar][remain] = ans

        return dp[0][0][k]


class Solution2:
    """
    leetcode solution 3: Space-Optimized Dynamic Programming
    Time: O(n * m^2 * k)
    Space: O(m * k)
    Runtime: 778 ms, faster than 69.52% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    Memory Usage: 16.4 MB, less than 98.10% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    """

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        prev_dp = [[0] * (k + 1) for _ in range(m + 1)]
        MOD = 10 ** 9 + 7

        for num in range(len(prev_dp)):
            prev_dp[num][0] = 1

        for i in range(n - 1, -1, -1):
            dp = [[0] * (k + 1) for _ in range(m + 1)]
            for max_so_far in range(m, -1, -1):
                for remain in range(k + 1):
                    ans = (max_so_far * prev_dp[max_so_far][remain]) % MOD

                    if remain > 0:
                        for num in range(max_so_far + 1, m + 1):
                            ans = (ans + prev_dp[num][remain - 1]) % MOD

                    dp[max_so_far][remain] = ans

            prev_dp = dp

        return dp[0][k]


class Solution3:
    """
    leetcode solution 4: A Different DP + Prefix Sums
    Time: O(n * m * k)
    Space: O(n * m * k)
    Runtime: 199 ms, faster than 82.86% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    Memory Usage: 24.2 MB, less than 55.24% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    """

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]
        prefix = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]
        MOD = 10 ** 9 + 7

        for num in range(1, m + 1):
            dp[1][num][1] = 1
            prefix[1][num][1] = prefix[1][num - 1][1] + 1

        for i in range(1, n + 1):
            for max_num in range(1, m + 1):
                for cost in range(1, k + 1):
                    ans = (max_num * dp[i - 1][max_num][cost]) % MOD
                    ans = (ans + prefix[i - 1][max_num - 1][cost - 1]) % MOD

                    dp[i][max_num][cost] += ans
                    dp[i][max_num][cost] %= MOD

                    prefix[i][max_num][cost] = (
                        prefix[i][max_num - 1][cost] + dp[i][max_num][cost]) % MOD

        return prefix[n][m][k]


class Solution4:
    """
    leetcode solution 5: Space-Optimized Better DP
    Time: O(n * m * k)
    Space: O(m * k)
    Runtime: 152 ms, faster than 92.38% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    Memory Usage: 16.6 MB, less than 94.29% of Python3 online submissions for Build Array Where You Can Find The Maximum Exactly K Comparisons.
    """

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        prefix = [[0] * (k + 1) for _ in range(m + 1)]
        prevDp = [[0] * (k + 1) for _ in range(m + 1)]
        prevPrefix = [[0] * (k + 1) for _ in range(m + 1)]
        MOD = 10 ** 9 + 7

        for num in range(1, m + 1):
            dp[num][1] = 1

        for i in range(1, n + 1):
            if i > 1:
                dp = [[0] * (k + 1) for _ in range(m + 1)]

            prefix = [[0] * (k + 1) for _ in range(m + 1)]
            for max_num in range(1, m + 1):
                for cost in range(1, k + 1):
                    ans = (max_num * prevDp[max_num][cost]) % MOD
                    ans = (ans + prevPrefix[max_num - 1][cost - 1]) % MOD

                    dp[max_num][cost] += ans
                    dp[max_num][cost] %= MOD

                    prefix[max_num][cost] = (
                        prefix[max_num - 1][cost] + dp[max_num][cost]) % MOD

            prevDp = dp
            prevPrefix = prefix

        return prefix[m][k]
