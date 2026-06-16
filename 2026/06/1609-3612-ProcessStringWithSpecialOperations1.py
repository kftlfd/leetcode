"""
Leetcode
2026-06-16
3612. Process String with Special Operations I
Medium

You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.

Build a new string result by processing s according to the following rules from left to right:

    If the letter is a lowercase English letter append it to result.
    A '*' removes the last character from result, if it exists.
    A '#' duplicates the current result and appends it to itself.
    A '%' reverses the current result.

Return the final string result after processing all characters in s.

 

Example 1:

Input: s = "a#b%*"

Output: "ba"

Explanation:
i	s[i]	Operation	Current result
0	'a'	Append 'a'	"a"
1	'#'	Duplicate result	"aa"
2	'b'	Append 'b'	"aab"
3	'%'	Reverse result	"baa"
4	'*'	Remove the last character	"ba"

Thus, the final result is "ba".

Example 2:

Input: s = "z*#"

Output: ""

Explanation:
i	s[i]	Operation	Current result
0	'z'	Append 'z'	"z"
1	'*'	Remove the last character	""
2	'#'	Duplicate the string	""

Thus, the final result is "".

 

Constraints:

    1 <= s.length <= 20
    s consists of only lowercase English letters and special characters *, #, and %.


"""

from collections import deque


class Solution:
    """
    Runtime 104ms Beats 6.58%
    Memory 33.34MB Beats 5.26%
    """

    def processStr(self, s: str) -> str:
        q = deque()

        for c in s:
            if c == "%":
                q.reverse()
            elif c == "*":
                if q:
                    q.pop()
            elif c == "#":
                q.extend(q)
            else:
                q.append(c)

        return "".join(q)


class Solution1:
    """
    leetcode solution
    Runtime 46ms Beats 21.05%
    Memory 29.91MB Beats 15.13%
    """

    def processStr(self, s: str) -> str:
        result = []
        for ch in s:
            if ch == "*":
                if result:
                    result.pop()
            elif ch == "#":
                result += result.copy()
            elif ch == "%":
                result = result[::-1]
            else:
                result.append(ch)
        return "".join(result)


class Solution2:
    """
    sample 0ms solution
    Runtime 0ms Beats 100.00%
    Memory 23.33MB Beats 72.37%
    """

    def processStr(self, s: str) -> str:
        ans = ""

        for x in s:
            if x == '*':
                ans = ans[:-1]

            elif x == '#':
                ans += ans

            elif x == '%':
                ans = ans[::-1]

            else:
                ans += x

        return ans
