"""
Leetcode
2025-06-27
2014. Longest Subsequence Repeated k Times
Hard

You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.

    For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".

Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

 

Example 1:
example 1

Input: s = "letsleetcode", k = 2
Output: "let"
Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
"let" is the lexicographically largest one.

Example 2:

Input: s = "bb", k = 2
Output: "b"
Explanation: The longest subsequence repeated 2 times is "b".

Example 3:

Input: s = "ab", k = 2
Output: ""
Explanation: There is no subsequence repeated 2 times. Empty string is returned.

 

Constraints:

    n == s.length
    2 <= n, k <= 2000
    2 <= n < k * 8
    s consists of lowercase English letters.


Hint 1
The length of the longest subsequence does not exceed n/k. Do you know why?
Hint 2
Find the characters that could be included in the potential answer. A character occurring more than or equal to k times can be used in the answer up to (count of the character / k) times.
Hint 3
Try all possible candidates in reverse lexicographic order, and check the string for the subsequence condition.
"""

from collections import deque
from typing import Counter, List


class Solution:
    """
    Time Limit Exceeded 305 / 313 testcases passed
    """

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        subs_len = n // k
        cnt = Counter(s)
        candidates = sorted(
            (-ord(c), count // k) for c, count in cnt.items() if count >= k
        )
        chars_left = [0] * 26
        for i, count in candidates:
            chars_left[-i-97] = count
        for cur_len in range(subs_len, 0, -1):
            for subs in self.get_subsequences("", cur_len, chars_left):
                full_subs = subs * k
                if self.is_subsequence_of(full_subs, s):
                    return subs
        return ""

    def get_subsequences(self, cur: str, l: int, chars_left: List[int]):
        if l < 1:
            yield cur
        for i in range(25, -1, -1):
            if chars_left[i] < 1:
                continue
            chars_left[i] -= 1
            yield from self.get_subsequences(cur + chr(i + 97), l - 1, chars_left)
            chars_left[i] += 1

    def is_subsequence_of(self, subs: str, string: str) -> bool:
        i = 0
        n = len(string)
        for c in subs:
            while i < n and string[i] != c:
                i += 1
            if i >= n:
                return False
            i += 1
        return True


class Solution1:
    """
    leetcode solution: Brute-force Enumeration
    Runtime 914ms Beats 54.47%
    Memory 17.96MB Beats 59.35%
    """

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        candidate = sorted(
            [c for c, w in Counter(s).items() if w >= k], reverse=True
        )
        q = deque(candidate)
        while q:
            curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr
            # generate the next candidate string
            for ch in candidate:
                nxt = curr + ch
                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)
        return ans
