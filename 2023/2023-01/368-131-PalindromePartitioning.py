"""
Leetcode
131. Palindrome Partitioning (medium)
2023-01-22

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""

from typing import List, Optional


# leetcode solution - Backtracking with Dynamic Programming
# Runtime: 852 ms, faster than 40.66% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 30.3 MB, less than 46.86% of Python3 online submissions for Palindrome Partitioning.
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        l = len(s)
        dp = [[False for _ in range(l)] for _ in range(l)]
        result = []

        def dfs(start: int, currList: List[str]):

            if start >= len(s):
                result.append(currList[:])

            for end in range(start, len(s)):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    currList.append(s[start:end+1])
                    dfs(end+1, currList)
                    currList.pop()

        dfs(0, [])
        return result


s = Solution()
tests = [
    ("abbab",
     [["a", "b", "b", "a", "b"], ["a", "b", "bab"], ["a", "bb", "a", "b"], ["abba", "b"]]),

    ("aab",
     [["a", "a", "b"], ["aa", "b"]]),

    ("a",
     [["a"]]),
]
for inp, exp in tests:
    res = s.partition(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
