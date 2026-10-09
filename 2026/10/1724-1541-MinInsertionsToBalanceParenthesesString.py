"""
Leetcode
2026-10-09
1541. Minimum Insertions to Balance a Parentheses String
Medium

Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

    Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
    Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

    For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

 

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

 

Constraints:

    1 <= s.length <= 105
    s consists of '(' and ')' only.


Hint 1
Use a stack to keep opening brackets. If you face single closing ')' add 1 to the answer and consider it as '))'.
Hint 2
If you have '))' with empty stack, add 1 to the answer, If after finishing you have x opening remaining in the stack, add 2x to the answer.
"""


class Solution:
    """
    Runtime 94ms Beats 16.84%
    Memory 19.84MB Beats 59.30%
    """

    def minInsertions(self, s: str) -> int:
        n = len(s)
        ans = 0
        cnt = 0
        i = 0

        while i < n:
            c = s[i]
            nxt = s[i + 1] if i + 1 < n else None

            if c == "(":
                cnt += 1
                i += 1
                continue

            if nxt == ")":
                i += 1
            else:
                ans += 1

            if cnt > 0:
                cnt -= 1
            else:
                ans += 1

            i += 1

        return ans + cnt * 2


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 64ms Beats 66.32%
    Memory 19.74MB Beats 88.77%
    """

    def minInsertions(self, s: str) -> int:
        length = len(s)
        insertions = left_count = index = 0

        while index < length:
            if s[index] == "(":
                left_count += 1
                index += 1
            else:
                if left_count > 0:
                    left_count -= 1
                else:
                    insertions += 1
                if index < length - 1 and s[index + 1] == ")":
                    index += 2
                else:
                    insertions += 1
                    index += 1

        insertions += left_count * 2
        return insertions
