"""
Leetcode
32. Longest Valid Parentheses (hard)
2022-05-24

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
"""



# leetcode solution 4 - https://leetcode.com/problems/longest-valid-parentheses/solution/
# Runtime: 81 ms, faster than 22.44% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 14 MB, less than 99.13% of Python3 online submissions for Longest Valid Parentheses.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        left = 0
        right = 0
        
        # go from left to right
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                ans = max(ans, 2*right)
            elif right > left:
                left = 0
                right = 0
                
        # go from right to left
        left = 0
        right = 0
        for i in range(len(s))[::-1]:
            if s[i] == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                ans = max(ans, 2*left)
            elif right < left:
                left = 0
                right = 0
                
        return ans



s = Solution()
tests = [
    "(()",
    ")()())",
    ""
]
for t in tests:
    print(t)
    print(s.longestValidParentheses(t))
    print()
