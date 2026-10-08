"""
Leetcode
2026-10-08
1021. Remove Outermost Parentheses
Easy

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is either '(' or ')'.
    s is a valid parentheses string.

"""


class Solution:
    """
    Runtime 7ms Beats 5.54%
    Memory 19.25MB Beats 70.87%
    """

    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        cnt = 0
        start_i = -1

        for i, c in enumerate(s):
            if c == "(":
                cnt += 1
            else:
                cnt -= 1

            if cnt == 1 and start_i == -1:
                start_i = i
            elif cnt == 0:
                ans.append(s[start_i+1:i])
                start_i = -1

        return "".join(ans)


class Solution1:
    """
    leetcode solution 1: Stack
    Runtime 0ms Beats 100.00%
    Memory 19.12MB Beats 93.67%
    """

    def removeOuterParentheses(self, s: str) -> str:
        res, stack = [], []
        for c in s:
            if c == ")":
                stack.pop()
            if stack:
                res.append(c)
            if c == "(":
                stack.append(c)
        return "".join(res)


class Solution2:
    """
    leetcode solution 2: Counting
    Runtime 0ms Beats 100.00%
    Memory 19.23MB Beats 70.87%
    """

    def removeOuterParentheses(self, s: str) -> str:
        res, level = [], 0
        for c in s:
            if c == ")":
                level -= 1
            if level > 0:
                res.append(c)
            if c == "(":
                level += 1
        return "".join(res)
