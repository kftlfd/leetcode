"""
Leetcode
2025-11-25
1015. Smallest Integer Divisible by K
Medium

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

 

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.

Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.

Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.

 

Constraints:

    1 <= k <= 10^5

 
Hint 1
11111 = 1111 * 10 + 1 We only need to store remainders modulo K.
Hint 2
If we never get a remainder of 0, why would that happen, and how would we know that?
"""


class Solution:
    """
    Runtime 976ms Beats 17.69%
    Memory 18.03MB Beats 26.46%
    """

    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        n = 1
        length = 1
        while n < k:
            n = (n * 10) + 1
            length += 1

        while n % k != 0:
            n = (n * 10) + 1
            length += 1

        return length


class Solution1:
    """
    leetcode solution
    Runtime 13ms Beats 38.02%
    Memory 17.61MB Beats 93.73%
    """

    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0

        for length_N in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length_N

        return -1
