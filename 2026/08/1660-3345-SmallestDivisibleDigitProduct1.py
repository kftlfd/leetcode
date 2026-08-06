"""
Leetcode
2026-08-06
3345. Smallest Divisible Digit Product I
Easy

You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

 

Example 1:

Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:

Input: n = 15, t = 3

Output: 16

Explanation:

The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

 

Constraints:

    1 <= n <= 100
    1 <= t <= 10


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.27MB Beats 73.98%
    """

    def smallestNumber(self, n: int, t: int) -> int:
        while n < 10 and n % t != 0:
            n += 1
        while (n // 10) * (n % 10) % t != 0:
            n += 1
        return n


class Solution1:
    """
    leetcode solution
    Runtime 3ms Beats 17.48%
    Memory 19.39MB Beats 32.93%
    """

    def smallestNumber(self, n: int, t: int) -> int:
        def check(num: int) -> bool:
            product = 1
            while num > 0:
                product *= num % 10
                num //= 10
                if product == 0:
                    break
            return product % t == 0

        while not check(n):
            n += 1
        return n
