"""
Leetcode
402. Remove K Digits
Medium
2024-04-11

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

 

Constraints:

    1 <= k <= num.length <= 10^5
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.
"""


class Solution:
    """
    https://leetcode.com/problems/remove-k-digits/discuss/700059/Python-Very-detail-explanation-with-examples-using-stack/1272182
    Runtime: 50 ms, faster than 85.98% of Python3 online submissions for Remove K Digits.
    Memory Usage: 17.8 MB, less than 95.71% of Python3 online submissions for Remove K Digits.
    """

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"

        # stack is mono-stack of increasing digits in num,
        # removing k digits which are bigger than the digit next to it
        stack = []
        for n in num:

            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1

            if stack or n != "0":
                stack.append(n)

        # if left with only increasing digits, but still have some
        # available to remove, then remove biggest (from the end)
        if k:
            stack = stack[:-k]

        if not stack:
            return "0"

        return "".join(stack)
