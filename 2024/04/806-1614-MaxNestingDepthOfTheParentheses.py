"""
Leetcode
1614. Maximum Nesting Depth of the Parentheses
Easy
2024-04-04

A string is a valid parentheses string (denoted VPS) if it meets one of the following:

    It is an empty string "", or a single character not equal to "(" or ")",
    It can be written as AB (A concatenated with B), where A and B are VPS's, or
    It can be written as (A), where A is a VPS.

We can similarly define the nesting depth depth(S) of any VPS S as follows:

    depth("") = 0
    depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
    depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
    depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"
Output: 3

 

Constraints:

    1 <= s.length <= 100
    s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
    It is guaranteed that parentheses expression s is a VPS.
"""


class Solution:
    """
    Runtime: 38 ms, faster than 37.13% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
    Memory Usage: 16.6 MB, less than 38.30% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
    """

    def maxDepth(self, s: str) -> int:
        cur_depth = 0
        max_depth = 0

        for c in s:
            if c == "(":
                cur_depth += 1
            elif c == ")":
                cur_depth -= 1
            max_depth = max(max_depth, cur_depth)

        return max_depth
