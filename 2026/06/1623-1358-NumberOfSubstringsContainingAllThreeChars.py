"""
Leetcode
2026-06-30
1358. Number of Substrings Containing All Three Characters
Medium

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1

 

Constraints:

    3 <= s.length <= 5 x 10^4
    s only consists of a, b or c characters.


Hint 1
For each position we simply need to find the first occurrence of a/b/c on or after this position.
Hint 2
So we can pre-compute three link-list of indices of each a, b, and c.
"""


class Solution:
    """
    Wrong Answer
    """

    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        left_cnt = 0
        for i in range(2, n):
            cur = s[i-2:i+1]
            if not ("a" in cur and "b" in cur and "c" in cur):
                continue
            left = i - 2 - left_cnt
            right = n - 1 - i
            left_cnt += 1
            ans += 1 + left + right + left * right
        return ans


class Solution1:
    """
    leetcode solution 1: Sliding Window
    Runtime 294ms Beats 5.05%
    Memory 19.34MB Beats 85.27%
    """

    def numberOfSubstrings(self, s: str) -> int:
        left = right = total = 0
        # Track frequency of a, b, c
        freq = [0] * 3

        while right < len(s):
            # Add character at right pointer to frequency array
            freq[ord(s[right]) - ord("a")] += 1

            # While we have all required characters
            while self._has_all_chars(freq):
                # All substrings from current window to end are valid
                # Add count of valid substrings
                total += len(s) - right

                # Remove leftmost character and move left pointer
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

            right += 1

        return total

    def _has_all_chars(self, freq: list) -> bool:
        # Check if we have at least one of each character
        return all(f > 0 for f in freq)


class Solution2:
    """
    leetcode solution 2: Last Position Tracking
    Runtime 58ms Beats 93.23%
    Memory 19.50MB Beats 15.25%
    """

    def numberOfSubstrings(self, s: str) -> int:
        # Track last position of a, b, c
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            # Update last position of current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Add count of valid substrings ending at current position
            # If any character is missing, min will be -1
            # Else min gives leftmost required character position
            total += 1 + min(last_pos)

        return total
