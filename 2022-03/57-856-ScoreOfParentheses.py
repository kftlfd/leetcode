'''
Leetcode
856. Score of Parentheses (medium)
2022-03-17

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:
 - "()" has score 1.
 - AB has score A + B, where A and B are balanced parentheses strings.
 - (A) has score 2 * A, where A is a balanced parentheses string.

Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2

Example 3:
Input: s = "()()"
Output: 2
'''



# leetcode solution 2
# https://leetcode.com/problems/score-of-parentheses/solution/
# Runtime: 48 ms, faster than 38.82% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 13.8 MB, less than 70.86% of Python3 online submissions for Score of Parentheses.
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        st = [0]

        for c in s:

            if c == '(':
                st.append(0)

            else:
                v = 2 * st.pop()
                st[-1] += max(v, 1)
        
        return st[0]



# leetcode solution 3
# Runtime: 43 ms, faster than 53.48% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 13.9 MB, less than 70.86% of Python3 online submissions for Score of Parentheses.
class Solution1:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        bal = 0
        for i, x in enumerate(s):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if s[i-1] == '(':
                    ans += 1 << bal
        return ans



s = Solution1()
tests = [
    "()",
    "(())",
    "()()"
]
for t in tests:
    print(t)
    print('->', s.scoreOfParentheses(t), '\n')
