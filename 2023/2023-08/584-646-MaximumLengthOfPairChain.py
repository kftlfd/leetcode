"""
Leetcode
646. Maximum Length of Pair Chain (medium)
2023-08-26

You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].

Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

Constraints:

    n == pairs.length
    1 <= n <= 1000
    -1000 <= lefti < righti <= 1000
"""

from typing import List


class Solution:
    """
    Time limit exceeded
    """

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs)

        def dfs(index: int, pairs_count: int, last_el: int) -> int:
            if index >= len(pairs):
                return pairs_count

            can_pick = pairs[index][0] > last_el

            return max(
                # skip
                dfs(index + 1, pairs_count, last_el),

                # pick
                dfs(index + 1, pairs_count + 1,
                    pairs[index][1]) if can_pick else -1
            )

        return dfs(0, 0, -2000)


class Solution1:
    """
    leetcode solution 1: recursive DP
    Time: O(n^2)
    Space: O(n)
    Runtime: 2035 ms, faster than 26.89% of Python3 online submissions for Maximum Length of Pair Chain.
    Memory Usage: 17 MB, less than 35.43% of Python3 online submissions for Maximum Length of Pair Chain.
    """

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs)
        n = len(pairs)
        memo = [0] * n

        ans = 0
        for i in range(n):
            ans = max(ans, self.longestPairChain(i, pairs, n, memo))
        return ans

    def longestPairChain(self, i: int, pairs: List[List[int]], n: int, memo: List[int]) -> int:
        if memo[i] != 0:
            return memo[i]
        memo[i] = 1
        for j in range(i + 1, n):
            if pairs[i][1] < pairs[j][0]:
                memo[i] = max(
                    memo[i], 1 + self.longestPairChain(j, pairs, n, memo))
        return memo[i]


class Solution2:
    """
    leetcode solution 2: iterative DP
    Time: O(n^2)
    Space: O(n)
    Runtime: 1633 ms, faster than 39.45% of Python3 online submissions for Maximum Length of Pair Chain.
    Memory Usage: 16.9 MB, less than 65.60% of Python3 online submissions for Maximum Length of Pair Chain.
    """

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs)
        n = len(pairs)
        dp = [1] * n
        ans = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])

        return ans


class Solution3:
    """
    leetcode solution 3: greedy
    Time: O(n * log(n))
    Space: O(1)
    Runtime: 191 ms, faster than 96.13% of Python3 online submissions for Maximum Length of Pair Chain.
    Memory Usage: 16.8 MB, less than 65.60% of Python3 online submissions for Maximum Length of Pair Chain.
    """

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])
        curr = float('-inf')
        ans = 0

        for pair in pairs:
            if pair[0] > curr:
                ans += 1
                curr = pair[1]

        return ans


s = Solution()
tests = [
    ([[1, 2], [2, 3], [3, 4]],
     2),

    ([[1, 2], [7, 8], [4, 5]],
     3),
]
for inp, exp in tests:
    res = s.findLongestChain(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
