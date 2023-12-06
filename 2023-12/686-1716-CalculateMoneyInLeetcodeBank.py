"""
Leetcode
1716. Calculate Money in Leetcode Bank
Easy
2023-12-06

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
    Runtime: 33 ms, faster than 91.19% of Python3 online submissions for Calculate Money in Leetcode Bank.
    Memory Usage: 16.2 MB, less than 40.24% of Python3 online submissions for Calculate Money in Leetcode Bank.
    """

    def totalMoney(self, n: int) -> int:

        ans = 0

        weeks, days = divmod(n, 7)

        if weeks > 0:
            ans += (28 * weeks) + (7 * (weeks * (weeks - 1) // 2))

        if days > 0:
            ans += ((weeks + 1) * days) + (days * (days - 1) // 2)

        return ans
