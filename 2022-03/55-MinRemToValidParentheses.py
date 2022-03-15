'''
Leetcode
1249. Minimum Remove to Make Valid Parentheses (medium)
2022-03-15

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', 
in any positions ) so that the resulting parentheses string is valid 
and return any valid string.

Formally, a parentheses string is valid if and only if:
 - It is the empty string, contains only lowercase characters, or
 - It can be written as AB (A concatenated with B), where A and B are 
   valid strings, or
 - It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
'''



# try 1
# Runtime: 204 ms, faster than 30.66% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 15.8 MB, less than 66.40% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        if not s or s.isalpha(): return s

        # go through string
        stack = [c for c in s]
        unclosed = []
        i = 0
        started = False
        while i < len(stack):

            # skip non-brackets
            if stack[i] not in ['(', ')']: i += 1

            # remove every closed bracket before the first open bracket (if any)
            elif not started:
                if stack[i] == ')':
                    del stack[i]
                elif stack[i] == '(':
                    started = True
                    unclosed.append(i)
                    i += 1
            
            # remeber indexes of open brackets in [unclosed]
            # closed brackets cancel out last open bracket (pop unclosed)
            else:
                if stack[i] == '(':
                    unclosed.append(i)
                    i += 1
                elif unclosed and stack[i] == ')':
                    unclosed.pop()
                    i+= 1
                elif not unclosed and stack[i] == ')':
                    del stack[i]

        # remove unclosed open brackets (if any)
        if unclosed:
            for i in unclosed[::-1]:
                del stack[i]

        return "".join(stack)



# try 2, using counter
# Runtime: 136 ms, faster than 65.73% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 16.2 MB, less than 28.95% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:

        if not s: return s

        st = []

        # remove unmatched closed brackets
        opened = 0
        for c in s:
            if c == '(':
                opened += 1
                st.append(c)
            elif c == ')':
                if opened:
                    opened -= 1
                    st.append(c)
            else: st.append(c)

        # remove extra open brackets (from the end)
        if opened:
            i = 1
            while opened:
                if st[-i] == '(':
                    del st[-i]
                    opened -= 1
                else: i += 1

        return "".join(st)



s = Solution1()
tests = [
    "lee(t(c)o)de)",
    "a)b(c)d",
    "abcd",
    "))((",
    ")a)d)a)a(d(d)a(d(d)f(s(f)a(("
]
for t in tests:
    res = s.minRemoveToMakeValid(t)
    print("test:\t", t)
    print("->", len(t)-len(res), "\t", res, "\n")
