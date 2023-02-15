"""
Leetcode
989. Add to Array-Form of Integer (easy)
2023-02-15

The array-form of an integer num is an array representing its digits in left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
"""

from typing import List, Optional


class Solution:
    """
    Runtime: 7514 ms, faster than 5.02% of Python3 online submissions for Add to Array-Form of Integer.
    Memory Usage: 15 MB, less than 85.98% of Python3 online submissions for Add to Array-Form of Integer.
    """

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        num_int = 0
        n = len(num) - 1
        for digit in num:
            num_int += digit * (10**n)
            n -= 1

        num_int += k

        ans = []
        while num_int > 0:
            ans.insert(0, num_int % 10)
            num_int = num_int // 10

        return ans


class Solution1:
    """
    leetcode solution, modified
    Runtime: 249 ms, faster than 99.83% of Python3 online submissions for Add to Array-Form of Integer.
    Memory Usage: 14.8 MB, less than 98.04% of Python3 online submissions for Add to Array-Form of Integer.
    """

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        i = len(num) - 1
        carry = k

        while i >= 0 and carry > 0:
            carry, num[i] = divmod(num[i] + carry, 10)
            i -= 1

        if carry > 0:
            num = [int(c) for c in str(carry)] + num

        return num


s = Solution1()
tests = [
    (([1, 2, 0, 0], 34),
     [1, 2, 3, 4]),

    (([2, 7, 4], 181),
     [4, 5, 5]),

    (([2, 1, 5], 806),
     [1, 0, 2, 1])
]
for inp, exp in tests:
    res = s.addToArrayForm(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
