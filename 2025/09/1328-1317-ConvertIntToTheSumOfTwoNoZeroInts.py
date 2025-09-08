"""
Leetcode
2025-09-08
1317. Convert Integer to the Sum of Two No-Zero Integers
Easy

No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

    a and b are No-Zero integers.
    a + b = n

The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.

Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.

 

Constraints:

    2 <= n <= 104


Hint 1
Loop through all elements from 1 to n.
Hint 2
Choose A = i and B = n - i then check if A and B are both No-Zero integers.
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.89MB Beats 31.73%
    """

    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n - 1
        b = 1

        def has_zero(num: int) -> bool:
            return "0" in str(num)

        while has_zero(a) or has_zero(b):
            a -= 1
            b += 1

        return [a, b]


class Solution1:
    """
    leetcode solution
    Runtime 0ms Beats 100.00%
    Memory 17.63MB Beats 83.63%
    """

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for A in range(1, n):
            B = n - A
            if "0" not in str(A) + str(B):
                return [A, B]
        return []
