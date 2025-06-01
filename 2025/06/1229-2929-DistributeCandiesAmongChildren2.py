"""
Leetcode
2025-06-01
2929. Distribute Candies Among Children II
Medium

You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

 

Example 1:

Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

Example 2:

Input: n = 3, limit = 3
Output: 10
Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).

 

Constraints:

    1 <= n <= 10^6
    1 <= limit <= 10^6


Hint 1
We can enumerate the number of candies of one particular child, let it be i which means 0 <= i <= min(limit, n).
Hint 2
Suppose the 2nd child gets j candies. Then 0 <= j <= limit and i + j <= n.
Hint 3
The 3rd child will hence get n - i - j candies and we should have 0 <= n - i - j <= limit.
Hint 4
After some transformations, for each i, we have max(0, n - i - limit) <= j <= min(limit, n - i), each j corresponding to a solution. So the number of solutions for some i is max(min(limit, n - i) - max(0, n - i - limit) + 1, 0). Sum the expression for every i in [0, min(n, limit)].
"""


class Solution:
    """
    Runtime 5288ms Beats 8.22%
    Memory 17.65MB Beats 69.18%
    """

    def distributeCandies(self, n: int, limit: int) -> int:
        return sum(
            max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)
            for i in range(min(n, limit) + 1)
        )


class Solution1:
    """
    leetcode solution 1: Enumeration
    """

    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            ans += min(n - i, limit) - max(0, n - i - limit) + 1
        return ans


class Solution2:
    """
    leetcode solution 2: Inclusion-Exclusion Principle
    Runtime 39ms Beats 79.45%
    Memory 17.54MB Beats 92.47%
    """

    def distributeCandies(self, n: int, limit: int) -> int:
        def cal(x):
            if x < 0:
                return 0
            return x * (x - 1) // 2

        return (
            cal(n + 2)
            - 3 * cal(n - limit + 1)
            + 3 * cal(n - (limit + 1) * 2 + 2)
            - cal(n - 3 * (limit + 1) + 2)
        )
