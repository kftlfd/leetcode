"""
Leetcode
2025-08-11
2438. Range Product Queries of Powers
Medium

Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.

You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.

 

Example 1:

Input: n = 15, queries = [[0,1],[2,2],[0,3]]
Output: [2,4,64]
Explanation:
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.

Example 2:

Input: n = 2, queries = [[0,0]]
Output: [2]
Explanation:
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 109 + 7 is the same, so [2] is returned.

 

Constraints:

    1 <= n <= 10^9
    1 <= queries.length <= 10^5
    0 <= starti <= endi < powers.length


Hint 1
The powers array can be created using the binary representation of n.
Hint 2
Once powers is formed, the products can be taken using brute force.
"""

from typing import List


class Solution00:
    """
    Runtime 60ms Beats 66.46%
    Memory 47.62MB Beats 52.17%
    """

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = []

        while n > 0:
            cur, nxt = 1, 2
            while nxt <= n:
                cur, nxt = nxt, nxt * 2
            arr.insert(0, cur)
            n -= cur

        mod = 10**9 + 7
        pref_sum = arr[:]

        for i in range(1, len(pref_sum)):
            pref_sum[i] = pref_sum[i] * pref_sum[i - 1]

        ans = [0] * len(queries)

        for i, (left, right) in enumerate(queries):
            if left == 0:
                ans[i] = pref_sum[right] % mod
            else:
                ans[i] = (pref_sum[right] // pref_sum[left - 1]) % mod

        return ans


class Solution01:
    """
    Runtime 64ms Beats 64.60%
    Memory 47.63MB Beats 52.17%
    """

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = []

        i = 1
        while i <= n:
            if n & i:
                arr.append(i)
            i <<= 1

        mod = 10**9 + 7
        pref_sum = arr[:]

        for i in range(1, len(pref_sum)):
            pref_sum[i] = pref_sum[i] * pref_sum[i - 1]

        ans = [0] * len(queries)

        for i, (left, right) in enumerate(queries):
            if left == 0:
                ans[i] = pref_sum[right] % mod
            else:
                ans[i] = (pref_sum[right] // pref_sum[left - 1]) % mod

        return ans


class Solution2:
    """
    leetcode solution 2: Binary Decomposition + Prefix Product Preprocessing
    Runtime 14ms Beats 95.65%
    Memory 44.45MB Beats 96.89%
    """

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        bins, rep = [], 1
        while n > 0:
            if n % 2 == 1:
                bins.append(rep)
            n //= 2
            rep *= 2

        m = len(bins)
        results = [[0] * m for _ in range(m)]
        for i in range(m):
            cur = 1
            for j in range(i, m):
                cur = cur * bins[j] % mod
                results[i][j] = cur

        ans = []
        for left, right in queries:
            ans.append(results[left][right])
        return ans
