"""
Leetcode
1047. Remove All Adjacent Duplicates In String (easy)
2022-11-10

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
"""

from typing import List, Optional


# Runtime: 199 ms, faster than 45.46% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.8 MB, less than 86.70% of Python3 online submissions for Remove All Adjacent Duplicates In String.
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


s = Solution()
tests = [
    ("abbaca",
     "ca"),

    ("azxxzy",
     "ay"),
]
for inp, exp in tests:
    res = s.removeDuplicates(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
