"""
Leetcode
2026-09-27
1190. Reverse Substrings Between Each Pair of Parentheses
Medium

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


Hint 1
Find all brackets in the string.
Hint 2
Does the order of the reverse matter ?
Hint 3
The order does not matter.
"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.34MB Beats 29.73%
    """

    def reverseParentheses(self, s: str) -> str:
        st = [""]

        for c in s:
            if c == "(":
                st.append("")
            elif c == ")":
                cur = st.pop()
                st[-1] += cur[::-1]
            else:
                st[-1] += c

        return "".join(st)


class Solution2:
    """
    leetcode solution 2: Wormhole Teleportation technique
    Runtime 3ms Beats 54.55%
    Memory 19.33MB Beats 29.73%
    """

    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n

        # First pass: Pair up parentheses
        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
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
