'''
Leetcode
20. Valid Parentheses (easy)
2022-03-13

Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
 1. Open brackets must be closed by the same type of brackets.
 2. Open brackets must be closed in the correct order.
'''



# try 1
# Runtime: 59 ms, faster than 18.84% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.1 MB, less than 29.07% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:
            if c in ['(', '[', "{"]: stack.append(c)
            elif stack:
                if c == ')' and stack[-1] == '(': stack.pop()
                elif c == ']' and stack[-1] == '[': stack.pop()
                elif c == '}' and stack[-1] == '{': stack.pop()
                elif c in [')', ']', '}']: return False
            elif c in [')', ']', '}']: return False
        
        return len(stack) == 0



# try 2
# https://leetcode.com/problems/valid-parentheses/discuss/1843839/Python3-STACK-Explained
# assuming string consists ONLY of open and closed brackets
# Runtime: 36 ms, faster than 75.07% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 47.91% of Python3 online submissions for Valid Parentheses.
class Solution1:
    def isValid(self, s: str) -> bool:

        stack = []
        hm = {'(':')', '[':']', '{':'}'}

        for c in s:
            if c in hm: stack.append(c)
            else:
                if not stack or c != hm[stack[-1]]: return False
                stack.pop()
        
        return len(stack) == 0



s = Solution1()
tests = [
    "()",
    "()[]{}",
    "(]",
    ")",
    "{{}[][[[()]]]}",
    "{{}[][[[(])]]}",
    "(])"
]
for t in tests:
    print(t)
    print(s.isValid(t))
    print()
