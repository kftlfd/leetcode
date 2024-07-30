"""
Leetcode
1653. Minimum Deletions to Make String Balanced
Medium
2024-07-30

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

Hints:
- You need to find for every index the number of Bs before it and the number of A's after it
- You can speed up the finding of A's and B's in suffix and prefix using preprocessing
"""


class Solution:
    """
    Wrong Answer
    """

    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_after = [0] * n
        b_before = [0] * n
        for i in range(1, n):
            b_before[i] = b_before[i-1] + (s[i-1] == "b")
            a_after[-i-1] = a_after[-i] + (s[-i] == "a")

        r_a = 0
        r_b = 0
        for i in range(n):
            c, aa, bb = s[i], a_after[i], b_before[i] - r_b
            if c == "b" and (bb + 1) < aa:
                r_b += 1
            elif c == "a" and aa < bb:
                r_a += 1

        return r_a + r_b


class Solution1:
    """
    leetcode solution 1: Three-Pass Count Method ((modified))
    Runtime: 940 ms, faster than 6.34% of Python3 online submissions for Minimum Deletions to Make String Balanced.
    Memory Usage: 25.1 MB, less than 6.00% of Python3 online submissions for Minimum Deletions to Make String Balanced.
    """

    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        a_after = [0] * n
        b_before = [0] * n
        for i in range(1, n):
            b_before[i] = b_before[i-1] + (s[i-1] == "b")
            a_after[-i-1] = a_after[-i] + (s[-i] == "a")

        ans = n
        for aa, bb in zip(a_after, b_before):
            ans = min(ans, aa + bb)

        return ans


class Solution3:
    """
    leetcode solution 3: Two-Variable Method
    Runtime: 468 ms, faster than 38.34% of Python3 online submissions for Minimum Deletions to Make String Balanced.
    Memory Usage: 17.8 MB, less than 52.00% of Python3 online submissions for Minimum Deletions to Make String Balanced.
    """

    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_count = sum(1 for ch in s if ch == "a")

        b_count = 0
        min_deletions = n

        # Second pass: iterate through the string to compute minimum deletions
        for ch in s:
            if ch == "a":
                a_count -= 1
            min_deletions = min(min_deletions, a_count + b_count)
            if ch == "b":
                b_count += 1

        return min_deletions


class Solution6:
    """
    leetcode solution 6: Optimized DP
    Runtime: 230 ms, faster than 86.00% of Python3 online submissions for Minimum Deletions to Make String Balanced.
    Memory Usage: 17.6 MB, less than 92.33% of Python3 online submissions for Minimum Deletions to Make String Balanced.
    """

    def minimumDeletions(self, s: str) -> int:
        min_deletions = 0
        b_count = 0

        # min_deletions variable represents dp[i]
        for ch in s:
            if ch == "b":
                b_count += 1
            else:
                # Two cases: remove 'a' or keep 'a'
                min_deletions = min(min_deletions + 1, b_count)

        return min_deletions
