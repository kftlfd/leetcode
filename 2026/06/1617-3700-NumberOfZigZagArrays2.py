"""
Leetcode
2026-06-24
3700. Number of ZigZag Arrays II

You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

    Each element lies in the range [l, r].
    No two adjacent elements are equal.
    No three consecutive elements form a strictly increasing or strictly decreasing sequence.

Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

 

Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

    [4, 5, 4]
    [5, 4, 5]

Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

    [1, 2, 1], [1, 3, 1], [1, 3, 2]
    [2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
    [3, 1, 2], [3, 1, 3], [3, 2, 3]

All arrays meet the ZigZag conditions.

 

Constraints:

    3 <= n <= 10^9
    1 <= l < r <= 75


Hint 1
Use matrix exponentiation
Hint 2
Encode states in a vector of length 2*m where m = r - l + 1: first m entries = "next compare = down" for values, next m = "next compare = up".
Hint 3
Build a transition matrix T (size 2*m * 2*m): from an up,x state go to down,y for every y > x, and from down,x go to up,y for every y < x.
Hint 4
Use fast matrix exponentiation to compute T^(n-1), apply it to the initial vector (ones in the block for starting up and separately for starting down), sum final entries, and add both results (for n=1 return m).
"""


class Solution:
    """
    leetcode solution: Dynamic Programming + Matrix Exponentiation
    Runtime 8353ms Beats 34.48%
    Memory 20.69MB Beats 51.72%
    """

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m

        size = 2 * m
        u = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1
            for j in range(i + 1, m):
                u[i + m][j] = 1

        dp = [[1] * size]
        dp = self.powMul(u, n - 1, dp)
        ans = 0
        for i in range(size):
            ans = (ans + dp[0][i]) % self.MOD

        return ans

    MOD = 1_000_000_007

    def mul(self, a, b):
        n = len(a)
        m = len(b[0])
        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for k in range(len(a[0])):
                r = a[i][k]
                if r == 0:
                    continue
                for j in range(m):
                    res[i][j] = (res[i][j] + r * b[k][j]) % self.MOD
        return res

    def powMul(self, base, exp, res):
        while exp > 0:
            if exp & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            exp >>= 1
        return res
