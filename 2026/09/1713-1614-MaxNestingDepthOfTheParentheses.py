"""
Leetcode
2026-09-28
1614. Maximum Nesting Depth of the Parentheses
Easy

Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"

Output: 3

 

Constraints:

    1 <= s.length <= 100
    s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
    It is guaranteed that parentheses expression s is a VPS.


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.26MB Beats 50.40%
    """

    def maxDepth(self, s: str) -> int:
        cur = 0
        ans = 0

        for c in s:
            if c == "(":
                cur += 1
            elif c == ")":
                cur -= 1
            ans = max(ans, cur)

        return ans
