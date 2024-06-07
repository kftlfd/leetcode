"""
Leetcode
648. Replace Words
Medium
2024-06-07

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

 

Constraints:

    1 <= dictionary.length <= 1000
    1 <= dictionary[i].length <= 100
    dictionary[i] consists of only lower-case letters.
    1 <= sentence.length <= 10^6
    sentence consists of only lower-case letters and spaces.
    The number of words in sentence is in the range [1, 1000]
    The length of each word in sentence is in the range [1, 1000]
    Every two consecutive words in sentence will be separated by exactly one space.
    sentence does not have leading or trailing spaces.
"""

from typing import List


class Solution:
    """
    Runtime: 103 ms, faster than 69.86% of Python3 online submissions for Replace Words.
    Memory Usage: 32.6 MB, less than 49.36% of Python3 online submissions for Replace Words.
    """

    class Trie:

        class TrieNode:
            def __init__(self, is_root=False):
                self.is_root = is_root
                self.nxt = {}

        def __init__(self, words: List[str]):
            self.root = self.TrieNode()
            self.load(words)

        def load(self, words: List[str]):
            for word in words:
                cur = self.root
                for c in word:
                    if c not in cur.nxt:
                        cur.nxt[c] = self.TrieNode()
                    cur = cur.nxt[c]
                cur.is_root = True

        def get_root_index(self, word: str):
            root_index = -1
            cur = self.root
            for i, c in enumerate(word):
                if c not in cur.nxt:
                    break
                cur = cur.nxt[c]
                if cur.is_root:
                    root_index = i
                    break
            return root_index

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = self.Trie(dictionary)

        words = sentence.split(" ")

        for i, word in enumerate(words):
            root_index = trie.get_root_index(word)
            if root_index >= 0:
                words[i] = word[:root_index+1]

        return " ".join(words)
