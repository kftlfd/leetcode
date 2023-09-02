"""
Leetcode
2707. Extra Characters in a String (medium)
2023-09-02

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
"""

from typing import List
from functools import cache


class Solution:
    """
    leetcode solution 1: top down DP with Substring method
    Time: O(n^3)
    Space: O(n + m*k)
    n = len(s); m = average len of words in dictionary; k = len(dictionary)
    Runtime: 240 ms, faster than 71.82% of Python3 online submissions for Extra Characters in a String.
    Memory Usage: 16.7 MB, less than 49.86% of Python3 online submissions for Extra Characters in a String.
    """

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dic_set = set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0

            # to count this character as a left over character
            # move to index `start + 1`
            ans = dp(start + 1) + 1

            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dic_set:
                    ans = min(ans, dp(end + 1))

            return ans

        return dp(0)


class Solution1:
    """
    leetcode solution 2: bottom up DP with Substring method
    Time: O(n^3)
    Space: O(n + m*k)
    n = len(s); m = average len of words in dictionary; k = len(dictionary)
    Runtime: 207 ms, faster than 87.80% of Python3 online submissions for Extra Characters in a String.
    Memory Usage: 16.4 MB, less than 87.26% of Python3 online submissions for Extra Characters in a String.
    """

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dic_set = set(dictionary)
        dp = [0] * (len(s) + 1)

        for start in range(n-1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dic_set:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    @classmethod
    def build(cls, dictionary):
        root = cls()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = cls()
                node = node.children[char]
            node.is_word = True
        return root


class Solution2:
    """
    leetcode solution 3: top down DP with Trie
    Time: O(n^2 + m*k)
    Space: O(n + m*k)
    n = len(s); m = average len of words in dictionary; k = len(dictionary)
    Runtime: 235 ms, faster than 74.53% of Python3 online submissions for Extra Characters in a String.
    Memory Usage: 24.6 MB, less than 5.69% of Python3 online submissions for Extra Characters in a String.
    """

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = TrieNode.build(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0

            # to count this character as a left over character
            # move to index `start + 1`
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


class Solution3:
    """
    leetcode solution 4: bottom up DP with Trie
    Time: O(n^2 + m*k)
    Space: O(n + m*k)
    n = len(s); m = average len of words in dictionary; k = len(dictionary)
    Runtime: 180 ms, faster than 95.66% of Python3 online submissions for Extra Characters in a String.
    Memory Usage: 17.4 MB, less than 19.24% of Python3 online submissions for Extra Characters in a String.
    """

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = TrieNode.build(dictionary)
        dp = [0] * (n + 1)

        for start in range(n-1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]


sol = Solution()
tests = [
    (("leetscode", ["leet", "code", "leetcode"]),
     1),

    (("sayhelloworld", ["hello", "world"]),
     3),
]
for inp, exp in tests:
    res = sol.minExtraChar(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
