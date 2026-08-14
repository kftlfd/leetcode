"""
Leetcode
2026-08-14
3090. Maximum Length Substring With Two Occurrences
Easy


Given a string s, return the maximum length of a  such that it contains at most two occurrences of each character.

 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:

Input: s = "aaaa"

Output: 2

Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

 

Constraints:

    2 <= s.length <= 100
    s consists only of lowercase English letters.


"""


from collections import defaultdict


class Solution:
    """
    Runtime 7ms Beats 29.86%
    Memory 19.44MB Beats 5.40%
    """

    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        cnt = defaultdict(int)
        i = 0
        overflow_n = 0
        ans = 0

        for j in range(n):
            c_j = s[j]
            cnt[c_j] += 1
            if cnt[c_j] == 3:
                overflow_n += 1

            if overflow_n > 0:
                c_i = s[i]
                cnt[c_i] -= 1
                if cnt[c_i] == 2:
                    overflow_n -= 1
                i += 1

            if overflow_n == 0:
                ans = max(ans, j - i + 1)

        return ans


class Solution2:
    """
    leetcode solution 2: Sliding Window
    Runtime 0ms Beats 100.00%
    Memory 19.26MB Beats 60.10%
    """

    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26
        left = 0
        res = 0
        for right, c in enumerate(s):
            ch = ord(c) - ord("a")
            count[ch] += 1
            while count[ch] > 2:
                ch2 = ord(s[left]) - ord("a")
                count[ch2] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
