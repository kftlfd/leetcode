"""
Leetcode
131. Palindrome Partitioning
Medium
2024-05-22

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

 

Constraints:

    1 <= s.length <= 16
    s contains only lowercase English letters.
"""

from typing import List


class Solution:
    """
    leetcode solution - Backtracking with Dynamic Programming
    Runtime: 459 ms, faster than 73.99% of Python3 online submissions for Palindrome Partitioning.
    Memory Usage: 35.3 MB, less than 41.59% of Python3 online submissions for Palindrome Partitioning.
    """

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
