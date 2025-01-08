"""
Leetcode
2025-01-08
3042. Count Prefix and Suffix Pairs I
Easy

You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

    isPrefixAndSuffix(str1, str2) returns true if str1 is both a
    prefix
    and a
    suffix
    of str2, and false otherwise.

For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

 

Example 1:

Input: words = ["a","aba","ababa","aa"]
Output: 4
Explanation: In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.

Example 2:

Input: words = ["pa","papa","ma","mama"]
Output: 2
Explanation: In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is true.
i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is true.
Therefore, the answer is 2.  

Example 3:

Input: words = ["abab","ab"]
Output: 0
Explanation: In this example, the only valid index pair is i = 0 and j = 1, and isPrefixAndSuffix("abab", "ab") is false.
Therefore, the answer is 0.

 

Constraints:

    1 <= words.length <= 50
    1 <= words[i].length <= 10
    words[i] consists only of lowercase English letters.
"""

from typing import List


class Solution:
    """
    Runtime 11ms Beats 56.86%
    Memory 17.74MB Beats 23.73%
    """

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(
            int(self.isPrefixAndSuffix(str1, str2))
            for j, str2 in enumerate(words)
            for str1 in words[:j]
        )

    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        n = len(str1)
        return str2[:n] == str1 and str2[-n:] == str1


class Solution1:
    """
    sample 0ms solution
    Runtime 3ms Beats 99.38%
    Memory 17.96MB Beats 6.47%
    """

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count


class Solution2:
    """
    leetcode solution 2: Dual Trie
    Runtime 53ms Beats 5.08%
    Memory 17.94MB Beats 6.47%
    """

    class Trie:

        class Node:
            def __init__(self):
                self.links = [None] * 26

            # Check if the character is present in the current node
            def _contains(self, c: str) -> bool:
                return self.links[ord(c) - ord("a")] is not None

            # Insert a new node for the character
            def _put(self, c: str, node: 'Node') -> None:
                self.links[ord(c) - ord("a")] = node

            # Get the next node for the character
            def _next(self, c: str) -> 'Node':
                return self.links[ord(c) - ord("a")]

        def __init__(self):
            self.root = self.Node()

        # Insert a word into the Trie
        def insert(self, word: str) -> None:
            node = self.root
            for c in word:
                if not node._contains(c):
                    node._put(c, self.Node())
                node = node._next(c)

        # Check if the Trie contains a given prefix
        def starts_with(self, prefix: str) -> bool:
            node = self.root
            for c in prefix:
                if not node._contains(c):
                    return False
                node = node._next(c)
            return True

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        # Step 1: Iterate over each word
        for i in range(n):
            prefix_trie = self.Trie()
            suffix_trie = self.Trie()

            # Step 2: Insert the current word into the prefix Trie
            prefix_trie.insert(words[i])

            # Step 3: Reverse the word and insert it into the suffix Trie
            rev_word = words[i][::-1]
            suffix_trie.insert(rev_word)

            # Step 4: Iterate over all previous words
            for j in range(i):
                # Step 5: Skip words[j] if it is longer than words[i]
                if len(words[j]) > len(words[i]):
                    continue

                # Step 6: Extract the prefix and reversed prefix of words[j]
                prefix_word = words[j]
                rev_prefix_word = prefix_word[::-1]

                # Step 7: Check if words[j] is both a prefix and suffix of words[i]
                if prefix_trie.starts_with(
                    prefix_word
                ) and suffix_trie.starts_with(rev_prefix_word):
                    count += 1

        # Step 8: Return the total count of valid pairs
        return count
