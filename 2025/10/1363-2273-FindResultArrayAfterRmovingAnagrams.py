"""
Leetcode
2025-10-13
2273. Find Resultant Array After Removing Anagrams
Easy

You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.

In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

 

Example 1:

Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.

Example 2:

Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]
Explanation:
No two adjacent strings in words are anagrams of each other, so no operations are performed.

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.


Hint 1
Instead of removing each repeating anagram, try to find all the strings in words which will not be present in the final answer.
Hint 2
For every index i, find the largest index j < i such that words[j] will be present in the final answer.
Hint 3
Check if words[i] and words[j] are anagrams. If they are, then it can be confirmed that words[i] will not be present in the final answer.
"""

from collections import Counter
from itertools import groupby
from typing import List


class Solution01:
    """
    Runtime 25ms Beats 16.81%
    Memory 17.88MB Beats 47.41%
    """

    def removeAnagrams(self, words: List[str]) -> List[str]:
        st = [(words[0], Counter(words[0]))]
        n = len(words)

        for i in range(1, n):
            word = words[i]
            cnt = Counter(word)
            if cnt != st[-1][1]:
                st.append((word, cnt))

        return [v[0] for v in st]


class Solution02:
    """
    Runtime 20ms Beats 24.08%
    Memory 17.80MB Beats 76.67%
    """

    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = [words[0]]
        prev = Counter(words[0])

        for i in range(1, n):
            word = words[i]
            cnt = Counter(word)
            if cnt != prev:
                ans.append(word)
                prev = cnt

        return ans


class Solution1:
    """
    leetcode solution: Judge Individually
    Runtime 15ms Beats 29.35%
    Memory 17.80MB Beats 47.41%
    """

    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]  # result array
        n = len(words)

        # determine if two words are anagrams
        def compare(word1: str, word2: str) -> bool:
            freq = [0] * 26
            for ch in word1:
                freq[ord(ch) - ord("a")] += 1
            for ch in word2:
                freq[ord(ch) - ord("a")] -= 1
            return all(x == 0 for x in freq)

        for i in range(1, n):
            if compare(words[i], words[i - 1]):
                continue
            res.append(words[i])

        return res


class Solution2:
    """
    sample 3ms solution
    Runtime 6ms Beats 53.93%
    Memory 17.79MB Beats 76.67%
    """

    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]

        for index in range(1, len(words)):
            current = words[index]
            prev = words[index - 1]

            if sorted(current) != sorted(prev):
                res.append(current)

        return res


class Solution3:
    """
    sample 0ms solution
    Runtime 3ms Beats 89.63%
    Memory 17.54MB Beats 99.75%
    """

    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [next(g) for _, g in groupby(words, sorted)]
