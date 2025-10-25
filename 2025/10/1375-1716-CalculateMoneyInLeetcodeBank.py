"""
Leetcode
2025-10-25
1716. Calculate Money in Leetcode Bank
Easy

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

 

Constraints:

    1 <= n <= 1000


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.99MB Beats 16.22%
    """

    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        ans = 28 * weeks
        ans += sum(7 * i for i in range(1, weeks))
        ans += sum(range(weeks + 1, weeks + days + 1))
        return ans


class Solution2:
    """
    leetcode solution 2: Math
    Runtime 0ms Beats 100.00%
    Memory 17.89MB Beats 37.64%
    """

    def totalMoney(self, n: int) -> int:
        k = n // 7
        F = 28
        L = 28 + (k - 1) * 7
        arithmetic_sum = k * (F + L) // 2

        monday = 1 + k
        final_week = 0
        for day in range(n % 7):
            final_week += monday + day

        return arithmetic_sum + final_week
