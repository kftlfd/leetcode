"""
Leetcode
1190. Reverse Substrings Between Each Pair of Parentheses
Medium
2024-07-11

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"

Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

 

Constraints:

    1 <= s.length <= 2000
    s only contains lower case English characters and parentheses.
    It is guaranteed that all parentheses are balanced.
"""


class Solution:
    """
    Runtime: 34 ms, faster than 72.09% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
    Memory Usage: 16.6 MB, less than 40.89% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
    """

    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ')':
                stack.append(c)
                continue

            segm = []
            ch = stack.pop()
            while ch != '(':
                segm.append(ch)
                ch = stack.pop()

            stack += segm

        return "".join(stack)


class Solution2:
    """
    leetcode solution 2: Wormhole Teleportation technique
    Runtime: 26 ms, faster than 97.21% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
    Memory Usage: 16.6 MB, less than 40.89% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
    """

    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n

        # First pass: Pair up parentheses
        for i, c in enumerate(s):
            if c == "(":
                open_parentheses_indices.append(i)
            if c == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i

        # Second pass: Build the result string
        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index += direction

        return "".join(result)


sol = Solution()
tests = [
    ("(abcd)", "dcba"),
    ("(u(love)i)", "iloveu"),
    ("(ed(et(oc))el)", "leetcode")
]
for inp, exp in tests:
    res = sol.reverseParentheses(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
