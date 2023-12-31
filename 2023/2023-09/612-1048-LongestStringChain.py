"""
Leetcode
1048. Longest String Chain (medium)
2023-09-23

You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

    For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length <= 16
    words[i] only consists of lowercase English letters.
"""

from typing import List


class Solution:
    """
    Runtime: 155 ms, faster than 57.11% of Python3 online submissions for Longest String Chain.
    Memory Usage: 19 MB, less than 16.26% of Python3 online submissions for Longest String Chain.
    """

    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)
        words = sorted(words, key=len, reverse=True)
        chain_lens = {}
        max_chain = 1

        def get_chain_len(word: str) -> int:
            if not word or word not in words_set:
                return 0

            if word in chain_lens:
                return chain_lens[word]

            if len(word) == 1:
                return 1

            word_chain_len = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                word_chain_len = max(word_chain_len,
                                     1 + get_chain_len(prev_word))

            chain_lens[word] = word_chain_len
            return word_chain_len

        for word in words:
            max_chain = max(max_chain, get_chain_len(word))

        return max_chain
