"""
Leetcode
2025-06-17
3405. Count the Number of Arrays with K Matching Adjacent Elements
Hard

You are given three integers n, m, k. A good array arr of size n is defined as follows:

    Each element in arr is in the inclusive range [1, m].
    Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].

Return the number of good arrays that can be formed.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, m = 2, k = 1

Output: 4

Explanation:

    There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
    Hence, the answer is 4.

Example 2:

Input: n = 4, m = 2, k = 2

Output: 6

Explanation:

    The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
    Hence, the answer is 6.

Example 3:

Input: n = 5, m = 2, k = 0

Output: 2

Explanation:

    The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.

 

Constraints:

    1 <= n <= 10^5
    1 <= m <= 10^5
    0 <= k <= n - 1


Hint 1
The first position arr[0] has m choices.
Hint 2
For each of the remaining n - 1 indices, 0 < i < n, select k positions from left to right and set arr[i] = arr[i - 1].
Hint 3
For all other indices, set arr[i] != arr[i - 1] with (m - 1) choices for each of the n - 1 - k positions.
"""

from math import comb


class Solution:
    """
    Wrong Answer 103 / 809 testcases passed
    """

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        kk = comb(n - 1, k)
        ans = m * ((m - 1) ** (n - k)) * kk
        return ans % mod


class Solution1:
    """
    leetcode solution: Combinatorial Mathematics
    Runtime 22ms Beats 85.94%
    Memory 25.23MB Beats 25.00%
    """

    MOD = 10**9 + 7
    MX = 10**5

    fact = [0] * MX
    inv_fact = [0] * MX

    def qpow(self, x, n):
        res = 1
        while n:
            if n & 1:
                res = res * x % self.MOD
            x = x * x % self.MOD
            n >>= 1
        return res

    def init(self):
        if self.fact[0] != 0:
            return
        self.fact[0] = 1
        for i in range(1, self.MX):
            self.fact[i] = self.fact[i - 1] * i % self.MOD
        self.inv_fact[self.MX -
                      1] = self.qpow(self.fact[self.MX - 1], self.MOD - 2)
        for i in range(self.MX - 1, 0, -1):
            self.inv_fact[i - 1] = self.inv_fact[i] * i % self.MOD

    def comb(self, n, m):
        return self.fact[n] * self.inv_fact[m] % self.MOD * self.inv_fact[n - m] % self.MOD

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        self.init()
        return self.comb(n - 1, k) * m % self.MOD * self.qpow(m - 1, n - k - 1) % self.MOD
