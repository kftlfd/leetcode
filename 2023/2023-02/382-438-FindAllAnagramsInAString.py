"""
Leetcode
438. Find All Anagrams in a String (medium)
2023-02-05

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

from typing import List, Optional


class Solution:
    """
    Runtime: 91 ms, faster than 98.30% of Python3 online submissions for Find All Anagrams in a String.
    Memory Usage: 15.2 MB, less than 74.41% of Python3 online submissions for Find All Anagrams in a String.
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []

        def get_letter_ht():
            ht = {}
            for i in range(ord('a'), ord('z') + 1):
                ht[chr(i)] = 0
            return ht

        # counter to check against
        letters_p = get_letter_ht()
        for c in p:
            letters_p[c] += 1

        # counter in window
        letters_s = get_letter_ht()
        for c in s[:len(p)]:
            letters_s[c] += 1

        ans = []

        if letters_s == letters_p:
            ans.append(0)

        # sliding window
        left = 0
        right = len(p)
        while right < len(s):
            letters_s[s[left]] -= 1
            letters_s[s[right]] += 1
            left += 1
            right += 1
            if letters_s == letters_p:
                ans.append(left)

        return ans


s = Solution()
tests = [
    (("cbaebabacd", "abc"),
     [0, 6]),

    (("abab", "ab"),
     [0, 1, 2]),
]
for inp, exp in tests:
    res = s.findAnagrams(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
