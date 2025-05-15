"""
Leetcode
2025-05-15
2900. Longest Unequal Adjacent Groups Subsequence I
Easy
Topics
Companies
Hint

You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].

Your task is to select the longest alternating

from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.

Return the selected subsequence. If there are multiple answers, return any of them.

Note: The elements in words are distinct.

 

Example 1:

Input: words = ["e","a","b"], groups = [0,0,1]

Output: ["e","b"]

Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2]. Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2]. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.

Example 2:

Input: words = ["a","b","c","d"], groups = [1,0,1,1]

Output: ["a","b","c"]

Explanation: A subsequence that can be selected is ["a","b","c"] because groups[0] != groups[1] and groups[1] != groups[2]. Another subsequence that can be selected is ["a","b","d"] because groups[0] != groups[1] and groups[1] != groups[3]. It can be shown that the length of the longest subsequence of indices that satisfies the condition is 3.

 

Constraints:

    1 <= n == words.length == groups.length <= 100
    1 <= words[i].length <= 10
    groups[i] is either 0 or 1.
    words consists of distinct strings.
    words[i] consists of lowercase English letters.


Hint 1
This problem can be solved greedily.
Hint 2
Begin by constructing the answer starting with the first number in groups.
Hint 3
For each index i in the range [1, n - 1], add i to the answer if groups[i] != groups[i - 1].
"""

from typing import List


class Solution00:
    """
    Runtime 3ms Beats 28.03%
    Memory 17.79MB Beats 65.57%
    """

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans0 = self.getAns(words, groups, 0)
        ans1 = self.getAns(words, groups, 1)
        if len(ans0) > len(ans1):
            return ans0
        return ans1

    def getAns(self, words: List[str], groups: List[int], nxt: int) -> List[str]:
        ans = []
        for c, g in zip(words, groups):
            if g == nxt:
                ans.append(c)
                nxt ^= 1
        return ans


class Solution01:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.76MB Beats 65.57%
    """

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        nxt = groups[0]
        for c, g in zip(words, groups):
            if g == nxt:
                ans.append(c)
                nxt ^= 1
        return ans


class Solution1:
    """
    leetcode solution 1: Dynamic Programming
    Runtime 7ms Beats 11.25%
    Memory 17.84MB Beats 39.10%
    """

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        max_len, end_index = 1, 0

        for i in range(1, n):
            best_len, best_prev = 1, -1
            for j in range(i - 1, -1, -1):
                if groups[i] != groups[j] and dp[j] + 1 > best_len:
                    best_len, best_prev = dp[j] + 1, j
            dp[i] = best_len
            prev[i] = best_prev
            if dp[i] > max_len:
                max_len, end_index = dp[i], i

        res = []
        i = end_index
        while i != -1:
            res.append(words[i])
            i = prev[i]
        return res[::-1]


class Solution2:
    """
    leetcode solution 2: Greedy
    Runtime 0ms Beats 100.00%
    Memory 17.79MB Beats 65.57%
    """

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return [words[0]] + [words[i] for i in range(1, len(groups)) if groups[i] != groups[i - 1]]
