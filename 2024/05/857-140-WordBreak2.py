"""
Leetcode
140. Word Break II
Hard
2024-05-25

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

 

Constraints:

    1 <= s.length <= 20
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 10
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
    Input is generated in a way that the length of the answer doesn't exceed 105.
"""

from typing import List


class TrieNode:
    def __init__(self, is_word: bool = False):
        self.is_word = is_word
        self.nxt = {}


class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for w in words:
            self.add(w)

    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.nxt:
                cur.nxt[c] = TrieNode()
            cur = cur.nxt[c]
        cur.is_word = True

    def check(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.nxt:
                return False
            cur = cur.nxt[c]
        return cur.is_word


class Solution:
    """
    Runtime: 44 ms, faster than 6.58% of Python3 online submissions for Word Break II.
    Memory Usage: 16.6 MB, less than 11.90% of Python3 online submissions for Word Break II.
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = Trie(wordDict)
        ans = []

        def dfs(start: int, cur: List[str]):
            if start == n:
                ans.append(" ".join(cur))
                return

            for end in range(start+1, n+1):
                cur_word = s[start:end]
                if words.check(cur_word):
                    cur.append(cur_word)
                    dfs(end, cur)
                    cur.pop()

        dfs(0, [])
        return ans


class Solution1:
    """
    leetcode solution 1: Backtracking
    Runtime: 37 ms, faster than 42.81% of Python3 online submissions for Word Break II.
    Memory Usage: 16.6 MB, less than 43.69% of Python3 online submissions for Word Break II.
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        results = []
        # Start the backtracking process
        self._backtrack(s, word_set, [], results, 0)
        return results

    def _backtrack(
        self,
        s: str,
        word_set: set,
        current_sentence: List[str],
        results: List[str],
        start_index: int,
    ):
        # If we've reached the end of the string, add the current sentence to results
        if start_index == len(s):
            results.append(" ".join(current_sentence))
            return

        # Iterate over possible end indices
        for end_index in range(start_index + 1, len(s) + 1):
            word = s[start_index:end_index]
            # If the word is in the set, proceed with backtracking
            if word in word_set:
                current_sentence.append(word)
                # Recursively call backtrack with the new end index
                self._backtrack(
                    s, word_set, current_sentence, results, end_index
                )
                # Remove the last word to backtrack
                current_sentence.pop()


class Solution2:
    """
    leetcode solution 2: Dynamic Programming - Memoization
    Runtime: 33 ms, faster than 72.16% of Python3 online submissions for Word Break II.
    Memory Usage: 16.4 MB, less than 87.62% of Python3 online submissions for Word Break II.
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memoization = {}
        return self._dfs(s, word_set, memoization)

    # Depth-first search function to find all possible word break combinations
    def _dfs(
        self, remaining_str: str, word_set: set, memoization: dict
    ) -> List[str]:
        # Check if result for this substring is already memoized
        if remaining_str in memoization:
            return memoization[remaining_str]
        # Base case: when the string is empty, return a list containing an empty string
        if not remaining_str:
            return [""]
        results = []
        for i in range(1, len(remaining_str) + 1):
            current_word = remaining_str[:i]
            # If the current substring is a valid word
            if current_word in word_set:
                for next_word in self._dfs(
                    remaining_str[i:], word_set, memoization
                ):
                    # Append current word and next word with space in between if next word exists
                    results.append(
                        current_word + (" " if next_word else "") + next_word
                    )
        # Memoize the results for the current substring
        memoization[remaining_str] = results
        return results


class Solution4:
    """
    leetcode solution 4: Trie Optimization
    Runtime: 31 ms, faster than 80.14% of Python3 online submissions for Word Break II.
    Memory Usage: 16.5 MB, less than 43.69% of Python3 online submissions for Word Break II.
    """

    class Trie:

        class TrieNode:
            def __init__(self):
                self.isEnd = False
                self.children = [None] * 26  # For lowercase English letters

        def __init__(self):
            self.root = self.TrieNode()

        def insert(self, word):
            node = self.root
            for char in word:
                index = ord(char) - ord("a")
                if not node.children[index]:
                    node.children[index] = self.TrieNode()
                node = node.children[index]
            node.isEnd = True

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Build the Trie from the word dictionary
        trie = self.Trie()
        for word in wordDict:
            trie.insert(word)

        # Map to store results of subproblems
        dp = {}

        # Iterate from the end of the string to the beginning
        for start_idx in range(len(s), -1, -1):
            # List to store valid sentences starting from start_idx
            valid_sentences = []

            # Initialize current node to the root of the trie
            current_node = trie.root

            # Iterate from start_idx to the end of the string
            for end_idx in range(start_idx, len(s)):
                char = s[end_idx]
                index = ord(char) - ord("a")

                # Check if the current character exists in the trie
                if not current_node.children[index]:
                    break

                # Move to the next node in the trie
                current_node = current_node.children[index]

                # Check if we have found a valid word
                if current_node.isEnd:
                    current_word = s[start_idx: end_idx + 1]

                    # If it's the last word, add it as a valid sentence
                    if end_idx == len(s) - 1:
                        valid_sentences.append(current_word)
                    else:
                        # If it's not the last word, append it to each sentence formed by the remaining substring
                        sentences_from_next_index = dp.get(end_idx + 1, [])
                        for sentence in sentences_from_next_index:
                            valid_sentences.append(
                                current_word + " " + sentence
                            )

            # Store the valid sentences in dp
            dp[start_idx] = valid_sentences

        # Return the sentences formed from the entire string
        return dp.get(0, [])


sol = Solution()
tests = [
    (("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
     ["cats and dog", "cat sand dog"]),

    (("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
     ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]),

    (("catsandog", ["cats", "dog", "sand", "and", "cat"]),
     []),
]
for inp, exp in tests:
    res = sol.wordBreak(*inp)
    s_exp = sorted(exp)
    s_res = sorted(res)
    if s_res != s_exp:
        print('input:  ', inp)
        print('expect: ', s_exp)
        print('output: ', s_res)
        print()
print('Completed testing')
