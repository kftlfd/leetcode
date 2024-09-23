"""
Leetcode
2024-09-23
2707. Extra Characters in a String
Medium

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

 

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

 

Constraints:

    1 <= s.length <= 50
    1 <= dictionary.length <= 50
    1 <= dictionary[i].length <= 50
    dictionary[i] and s consists of only lowercase English letters
    dictionary contains distinct words


Hints:
- Can we use Dynamic Programming here?
- Define DP[i] as the min extra character if breaking up s[0:i] optimally.
"""

from functools import cache
from typing import List


class Solution1:
    """
    leetcode solution 1: Top Down Dynamic Programming with Substring Method
    Runtime: 198 ms, faster than 61.47% of Python3 online submissions for Extra Characters in a String.
    Memory Usage: 17 MB, less than 46.06% of Python3 online submissions for Extra Characters in a String.
    """

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0
            # To count this character as a left over character
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
            return ans

        return dp(0)


class Solution2:
    """
    leetcode solution 2: Bottom Up Dynamic Programming with Substring Method
    """

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]


class Solution3:
    """
    leetcode solution 3: Top Down Dynamic Programming with Trie
    """

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = self.buildTrie(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0
            # To count this character as a left over character
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    ans = min(ans, dp(end + 1))
            return ans

        return dp(0)

    def buildTrie(self, dictionary):
        root = self.TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = self.TrieNode()
                node = node.children[char]
            node.is_word = True
        return root


class Solution4:
    """
    leetcode solution 4: Bottom Up Dynamic Programming with Trie
    """

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = self.buildTrie(dictionary)
        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]

    def buildTrie(self, dictionary):
        root = self.TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = self.TrieNode()
                node = node.children[char]
            node.is_word = True
        return root
