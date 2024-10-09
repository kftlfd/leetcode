"""
Leetcode
2024-10-09
921. Minimum Add to Make Parentheses Valid
Medium

A parentheses string is valid if and only if:

    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

    For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1

Example 2:

Input: s = "((("
Output: 3

 

Constraints:

    1 <= s.length <= 1000
    s[i] is either '(' or ')'.
"""


class Solution:
    """
    Runtime: 32 ms, faster than 75.60% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
    Memory Usage: 16.7 MB, less than 30.64% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
    """

    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        add = 0

        for c in s:
            if c == "(":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                add += 1
                balance = 0

        return balance + add


class Solution1:
    """
    leetcode solution
    Runtime: 33 ms, faster than 71.93% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
    Memory Usage: 16.6 MB, less than 30.64% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
    """

    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds_required += 1

        # Add the remaining open brackets as closing brackets would be required.
        return min_adds_required + open_brackets
