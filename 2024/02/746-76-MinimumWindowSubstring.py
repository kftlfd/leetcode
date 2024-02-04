"""
Leetcode
76. Minimum Window Substring
Hard
2024-02-04

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

 

Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

Hints:
- Use two pointers to create a window of letters in s, which would have all the characters from t.
- Expand the right pointer until all the characters of t are covered.
- Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.
- Continue expanding the right and left pointers until you reach the end of s.
"""

from collections import Counter


class Solution:
    """
    Runtime: 546 ms, faster than 9.17% of Python3 online submissions for Minimum Window Substring.
    Memory Usage: 17.2 MB, less than 90.66% of Python3 online submissions for Minimum Window Substring.
    """

    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_w = Counter()
        ans_start = 0
        ans_len = float('inf')

        win_left = 0
        for win_right, c in enumerate(s):
            count_w[c] += 1

            while all(count_w[c] >= n for c, n in count_t.items()):
                if win_right - win_left + 1 < ans_len:
                    ans_len = win_right - win_left + 1
                    ans_start = win_left
                count_w[s[win_left]] -= 1
                win_left += 1

        return "" if ans_len == float('inf') else s[ans_start:ans_start+ans_len]


sol = Solution()
tests = [
    (("ab", "b"),
     "b"),

    (("ADOBECODEBANC", "ABC"),
     "BANC"),

    (("a", "a"),
     "a"),

    (("a", "aa"),
     ""),
]
for inp, exp in tests:
    res = sol.minWindow(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
