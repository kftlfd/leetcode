"""
Leetcode
336. Palindrome Pairs (hard)
2022-09-17

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:
Input: words = ["a",""]
Output: [[0,1],[1,0]]
"""

from typing import List


# https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
# Runtime: 4579 ms, faster than 60.69% of Python3 online submissions for Palindrome Pairs.
# Memory Usage: 26.4 MB, less than 85.90% of Python3 online submissions for Palindrome Pairs.
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []

        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])

        return valid_pals


s = Solution()
tests = [
    ["abcd", "dcba", "lls", "s", "sssll"],
    ["bat", "tab", "cat"],
    ["a", ""],
]
for t in tests:
    print(t)
    print(s.palindromePairs(t))
    print()
