"""
Leetcode
879. Profitable Schemes (hard)
2023-04-21

There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.

Example 2:
Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2)
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/profitable-schemes/discuss/154617/C++JavaPython-DP
    Runtime: 1352 ms, faster than 75.24% of Python3 online submissions for Profitable Schemes.
    Memory Usage: 14.5 MB, less than 69.52% of Python3 online submissions for Profitable Schemes.
    """

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (n + 1) for i in range(minProfit + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(minProfit, -1, -1):
                for j in range(n - g, -1, -1):
                    dp[min(i + p, minProfit)][j + g] += dp[i][j]
        return sum(dp[minProfit]) % (10**9 + 7)


s = Solution()
tests = [
    ((5, 3, [2, 2], [2, 3]),
     2),

    ((10, 5, [2, 3, 5], [6, 7, 8]),
     7),
]
for inp, exp in tests:
    res = s.profitableSchemes(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
