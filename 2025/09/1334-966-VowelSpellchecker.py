"""
Leetcode
2025-09-14
966. Vowel Spellchecker
Medium

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

    Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
        Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
        Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
        Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
    Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
        Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
        Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
        Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)

In addition, the spell checker operates under the following precedence rules:

    When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
    When the query matches a word up to capitlization, you should return the first such match in the wordlist.
    When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
    If the query has no matches in the wordlist, you should return the empty string.

Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

Example 2:

Input: wordlist = ["yellow"], queries = ["YellOw"]
Output: ["yellow"]

 

Constraints:

    1 <= wordlist.length, queries.length <= 5000
    1 <= wordlist[i].length, queries[i].length <= 7
    wordlist[i] and queries[i] consist only of only English letters.


"""

from typing import List


class Solution:
    """
    Runtime 24ms Beats 96.88%
    Memory 20.20MB Beats 78.47%
    """

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wl_orig = {w: i for i, w in enumerate(wordlist)}

        wl_case = {}
        for i, w in enumerate(wordlist):
            v = w.lower()
            if v not in wl_case:
                wl_case[v] = i

        def to_vowel_mask(word: str) -> str:
            word = word.lower()
            for v in "aeiou":
                word = word.replace(v, "*")
            return word

        wl_vows = {}
        for i, w in enumerate(wordlist):
            v = to_vowel_mask(w)
            if v not in wl_vows:
                wl_vows[v] = i

        ans = [""] * len(queries)

        for i, q in enumerate(queries):
            if q in wl_orig:
                ans[i] = q
                continue

            low_case = q.lower()
            if low_case in wl_case:
                ans[i] = wordlist[wl_case[low_case]]
                continue

            vow_mask = to_vowel_mask(q)
            if vow_mask in wl_vows:
                ans[i] = wordlist[wl_vows[vow_mask]]

        return ans


class Solution1:
    """
    leetcode solution
    Runtime 43ms Beats 56.94%
    Memory 20.30MB Beats 30.03%
    """

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return list(map(solve, queries))
