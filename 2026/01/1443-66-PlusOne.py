"""
Leetcode
2026-01-01
66. Plus One
Easy

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

 

Constraints:

    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain any leading 0's.


"""

from typing import List


class Solution00:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.42MB Beats 82.42%
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits[:]
        i = len(digits) - 1
        res[i] += 1

        while res[i] > 9:
            res[i] = 0
            i -= 1
            if i < 0:
                res.insert(0, 1)
                break
            res[i] += 1

        return res


class Solution01:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.28MB Beats 91.11%
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        return list(map(int, str(num + 1)))


class Solution02:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.29MB Beats 91.11%
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num = num * 10 + d

        num += 1

        res = []
        while num > 0:
            res.insert(0, num % 10)
            num //= 10

        return res
