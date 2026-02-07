"""
Leetcode
2026-02-07
1653. Minimum Deletions to Make String Balanced
Solved
Medium
Topics
premium lock iconCompanies
Hint

You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is 'a' or 'b'.


Hint 1
You need to find for every index the number of Bs before it and the number of A's after it
Hint 2
You can speed up the finding of A's and B's in suffix and prefix using preprocessing
"""


class Solution:
    """
    Runtime 526ms Beats 27.67%
    Memory 24.34MB Beats 16.44%
    """

    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        ans = n
        a_left = 0
        b_right = [0] * n

        b_cnt = 0
        for i in range(n - 1, -1, -1):
            b_cnt += s[i] == "b"
            b_right[i] = b_cnt

        for i, c in enumerate(s):
            a_left += c == "a"
            ans = min(ans, n - (a_left + b_right[i]))

        return ans


class Solution1:
    """
    sample 121ms solution
    Runtime 123ms Beats 97.26%
    Memory 20.46MB Beats 33.97%
    """

    def minimumDeletions(self, s: str) -> int:
        res = count = 0
        for c in s:
            if c == 'b':
                count += 1
            elif count:
                res += 1
                count -= 1
        return res
