"""
Leetcode
2026-02-12
3713. Longest Balanced Substring I
Medium

You are given a string s consisting of lowercase English letters.

A of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

 

Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "zzabccy"

Output: 4

Explanation:

The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.

Example 3:

Input: s = "aba"

Output: 2

Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 

Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.


Hint 1
Use bruteforce over all substrings    
"""

from collections import Counter, defaultdict


class Solution01:
    """
    Time Limit Exceeded
    """

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n

        for length in range(n, 2, -1):
            for start in range(n - length + 1):
                substr = s[start:start + length]
                if self.is_balanced(substr):
                    return length

        return 2

    def is_balanced(self, s: str) -> bool:
        if len(s) < 3:
            return True

        cnt = Counter(s)
        t = cnt[s[0]]
        return all(count == t for count in cnt.values())


class Solution1:
    """
    leetcode solution: Enumeration
    Runtime 2650ms Beats 56.02%
    Memory 19.28MB Beats 62.89%
    """

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                if len(set(cnt.values())) == 1:
                    res = max(res, j - i + 1)
        return res
