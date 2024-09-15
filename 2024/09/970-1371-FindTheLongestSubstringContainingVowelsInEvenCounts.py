"""
Leetcode
2024-09-15
1371. Find the Longest Substring Containing Vowels in Even Counts
Medium

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.

Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

 

Constraints:

    1 <= s.length <= 5 x 10^5
    s contains only lowercase English letters.
"""


class Solution:
    """
    Runtime: 141 ms, faster than 91.92% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
    Memory Usage: 22.8 MB, less than 8.08% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
    """

    def findTheLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        v = {
            'a': 1,
            'e': 1 << 1,
            'i': 1 << 2,
            'o': 1 << 3,
            'u': 1 << 4
        }

        pref_sum = [0] * (s_len + 1)
        mask = 0

        for i, c in enumerate(s, start=1):
            mask ^= v.get(c, 0)
            pref_sum[i] = mask

        for l in range(s_len + 1):
            for start in range(l + 1):
                if pref_sum[start] ^ pref_sum[s_len - l + start] == 0:
                    return s_len - l

        return 0


class Solution1:
    """
    leetcode solution
    Runtime: 297 ms, faster than 66.57% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
    Memory Usage: 22 MB, less than 79.11% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
    """

    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longestSubstring = 0
        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i]) - ord("a")]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            longestSubstring = max(longestSubstring, i - mp[prefixXOR])
        return longestSubstring
