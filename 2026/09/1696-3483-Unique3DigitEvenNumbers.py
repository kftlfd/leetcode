"""
Leetcode
2026-09-11
3483. Unique 3-Digit Even Numbers
Easy

You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

 

Example 1:

Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

Example 2:

Input: digits = [0,2,2]

Output: 2

Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

Example 3:

Input: digits = [6,6,6]

Output: 1

Explanation: Only 666 can be formed.

Example 4:

Input: digits = [1,3,5]

Output: 0

Explanation: No even 3-digit numbers can be formed.

 

Constraints:

    3 <= digits.length <= 10
    0 <= digits[i] <= 9

 
"""

from typing import List


class Solution:
    """
    Runtime 12ms Beats 76.04%
    Memory 19.15MB Beats 92.09%
    """

    def totalNumbers(self, digits: List[int]) -> int:
        if all(d % 2 == 1 for d in digits):
            return 0

        n = len(digits)
        nums = set()

        def add_valid(num: int):
            if num >= 100 and num & 1 == 0:
                nums.add(num)

        def add_perms(a: int, b: int, c: int):
            add_valid(a * 100 + b * 10 + c)
            add_valid(a * 100 + c * 10 + b)
            add_valid(b * 100 + a * 10 + c)
            add_valid(b * 100 + c * 10 + a)
            add_valid(c * 100 + a * 10 + b)
            add_valid(c * 100 + b * 10 + a)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    add_perms(digits[i], digits[j], digits[k])

        return len(nums)


class Solution1:
    """
    leetcode solution
    Runtime 13ms Beats 72.75%
    Memory 19.52MB Beats 13.85%
    """

    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        vis = [False] * 1000
        ans = 0

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue
                    x = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if not vis[x]:
                        vis[x] = True
                        ans += 1

        return ans
