"""
Leetcode
1544. Make The String Great (easy)
2022-11-08

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

 - 0 <= i <= s.length - 2
 - s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"
"""

from typing import List, Optional


# leetcode solution - stack
# Runtime: 41 ms, faster than 89.65% of Python3 online submissions for Make The String Great.
# Memory Usage: 13.8 MB, less than 97.60% of Python3 online submissions for Make The String Great.
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


# leetcode solution - recursion
# Runtime: 62 ms, faster than 65.95% of Python3 online submissions for Make The String Great.
# Memory Usage: 13.9 MB, less than 61.93% of Python3 online submissions for Make The String Great.
class Solution1:
    def makeGood(self, s: str) -> str:
        # If we find a pair in 's', remove this pair from 's'
        # and solve the remaining string recursively.
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                return self.makeGood(s[:i] + s[i + 2:])
        return s


s = Solution()
tests = [
    ("leEeetcode",
     "leetcode"),

    ("abBAcC",
     ""),

    ("s",
     "s"),
]
for inp, exp in tests:
    res = s.makeGood(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
