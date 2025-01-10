"""
Leetcode
2025-01-10
916. Word Subsets
Solved
Medium
Topics
Companies

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

    For example, "wrr" is a subset of "warrior" but is not a subset of "world".

A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

 

Constraints:

    1 <= words1.length, words2.length <= 10^4
    1 <= words1[i].length, words2[i].length <= 10
    words1[i] and words2[i] consist only of lowercase English letters.
    All the strings of words1 are unique.
"""

from collections import Counter
from typing import List


class Solution01:
    """
    Time Limit Exceeded
    """

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w2_cnt = [Counter(w) for w in words2]
        return [w for w in words1 if self.is_universal(w, w2_cnt)]

    def is_universal(self, word: str, counters: List[Counter]) -> bool:
        cnt = Counter(word)
        for cnt2 in counters:
            for c, n in cnt2.items():
                if cnt[c] < n:
                    return False
        return True


class Solution02:
    """
    Runtime 363ms Beats 63.75%
    Memory 21.29MB Beats 21.91%
    """

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt2 = Counter()

        for w2 in words2:
            for c, n in Counter(w2).items():
                cnt2[c] = max(cnt2[c], n)

        def is_universal(w: str) -> bool:
            cnt = Counter(w)
            for c, n in cnt2.items():
                if cnt[c] < n:
                    return False
            return True

        return [w for w in words1 if is_universal(w)]


class Solution1:
    """
    leetcode solution
    Runtime 487ms Beats 39.84%
    Memory 21.20MB Beats 21.91%
    """

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in words2:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in words1:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans
