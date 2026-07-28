"""
Leetcode
2026-07-28
3517. Smallest Palindromic Rearrangement I
Medium

You are given a string s.

Return the palindromic of s.

 

Example 1:

Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.

Example 2:

Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:

Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

 

Constraints:

    1 <= s.length <= 10^5
    s consists of lowercase English letters.
    s is guaranteed to be palindromic.


Hint 1
Consider a palindrome as composed of two mirror-image halves.
Hint 2
Construct one half (using s), and then the other half is its reverse to obtain the lexicographically smallest permutation.
"""


from collections import Counter


class Solution:
    """
    Runtime 343ms Beats 28.57%
    Memory 21.48MB Beats 23.04%
    """

    def smallestPalindrome(self, s: str) -> str:
        ans = [""] * len(s)
        i = 0

        for c, n in sorted(Counter(s).items()):
            for _ in range(n // 2):
                ans[i] = ans[-1 - i] = c
                i += 1
            if n & 1 == 1:
                ans[len(s) // 2] = c

        return "".join(ans)


class Solution1:
    """
    leetcode solution 1: Sorting
    Runtime 271ms Beats 50.69%
    Memory 22.17MB Beats 6.45%
    """

    def smallestPalindrome(self, s: str) -> str:
        partition = len(s) // 2

        base = sorted(s[:partition])
        mid = [s[partition]] if len(s) % 2 == 1 else []
        reversed_base = base[::-1]

        return "".join(base + mid + reversed_base)


class Solution2:
    """
    leetcode solution 2: Counting Sort
    Runtime 130ms Beats 98.16%
    Memory 20.60MB Beats 96.31%
    """

    def smallestPalindrome(self, s: str) -> str:
        partition = len(s) // 2
        bucket = [0] * 26

        for i in range(partition):
            bucket[ord(s[i]) - 97] += 1

        left = "".join(
            [chr(i + 97) * bucket[i] for i in range(26) if bucket[i] > 0]
        )

        mid = s[partition] if len(s) % 2 != 0 else ""
        right = left[::-1]

        return left + mid + right
