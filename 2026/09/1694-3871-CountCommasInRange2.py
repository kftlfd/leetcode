"""
Leetcode
2026-09-09
3871. Count Commas in Range II
Medium

You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

    A comma is inserted after every three digits from the right.
    Numbers with fewer than 4 digits contain no commas.

 

Example 1:

Input: n = 1002

Output: 3

Explanation:

The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

Example 2:

Input: n = 998

Output: 0

Explanation:

All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

 

Constraints:

    1 <= n <= 10^15


"""


class Solution01:
    """
    Wrong Answer
    """

    def countCommas(self, n: int) -> int:
        if n < 1_000:
            return 0

        ans = 0
        g = 1_000
        commas = 0
        rem = 0

        while n >= g:
            ans += (g - 1_000) * commas
            rem = n - g
            g *= 1_000
            commas += 1

        ans += (rem + 1) * commas

        return ans


class Solution02:
    """
    Runtime 1ms Beats 26.53%
    Memory 19.12MB Beats 87.75%
    """

    def countCommas(self, n: int) -> int:
        if n < 1_000:
            return 0

        ans = 0
        commas = 1
        g_min = 1_000
        g_max = 999_999

        while True:
            ans += (min(n, g_max) - g_min + 1) * commas

            if n <= g_max:
                break

            commas += 1
            g_min *= 1_000
            g_max = g_max * 1_000 + 999

        return ans


class Solution1:
    """
    leetcode solution: Place Value Contribution
    Runtime 0ms Beats 100.00%
    Memory 19.11MB Beats 87.75%
    """

    def countCommas(self, n: int) -> int:
        # Numbers greater than or equal to 103 will contain at least 1 comma,
        # contributing a total of n−103+1 commas.
        # Numbers greater than or equal to 106 will contain at least 2 commas
        # (i.e., an additional 1 comma per number from the previous step),
        # contributing an additional n−106+1.
        # In general, each power of 1000 (p) up to n contributes an additional
        # n−p+1 commas.
        p = 1000
        res = 0
        while p <= n:
            res += n - p + 1
            p *= 1000
        return res
