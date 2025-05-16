"""
Leetcode
2025-05-16
2901. Longest Unequal Adjacent Groups Subsequence II
Medium

You are given a string array words, and an array groups, both arrays having length n.

The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.

You need to select the longest

from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:

    For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
    words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.

Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.

Note: strings in words may be unequal in length.

 

Example 1:

Input: words = ["bab","dab","cab"], groups = [1,2,2]

Output: ["bab","cab"]

Explanation: A subsequence that can be selected is [0,2].

    groups[0] != groups[2]
    words[0].length == words[2].length, and the hamming distance between them is 1.

So, a valid answer is [words[0],words[2]] = ["bab","cab"].

Another subsequence that can be selected is [0,1].

    groups[0] != groups[1]
    words[0].length == words[1].length, and the hamming distance between them is 1.

So, another valid answer is [words[0],words[1]] = ["bab","dab"].

It can be shown that the length of the longest subsequence of indices that satisfies the conditions is 2.

Example 2:

Input: words = ["a","b","c","d"], groups = [1,2,3,4]

Output: ["a","b","c","d"]

Explanation: We can select the subsequence [0,1,2,3].

It satisfies both conditions.

Hence, the answer is [words[0],words[1],words[2],words[3]] = ["a","b","c","d"].

It has the longest length among all subsequences of indices that satisfy the conditions.

Hence, it is the only answer.

 

Constraints:

    1 <= n == words.length == groups.length <= 1000
    1 <= words[i].length <= 10
    1 <= groups[i] <= n
    words consists of distinct strings.
    words[i] consists of lowercase English letters.


Hint 1
Let dp[i] represent the length of the longest subsequence ending with words[i] that satisfies the conditions.
Hint 2
dp[i] = (maximum value of dp[j]) + 1 for indices j < i, where groups[i] != groups[j], words[i] and words[j] are equal in length, and the hamming distance between words[i] and words[j] is exactly 1.
Hint 3
Keep track of the j values used to achieve the maximum dp[i] for each index i.
Hint 4
The expected array's length is max(dp[0:n]), and starting from the index having the maximum value in dp, we can trace backward to get the words.
"""

from typing import List


class Solution:
    """
    Runtime 1105ms Beats 47.73%
    Memory 17.94MB Beats 93.18%
    """

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[1, -1] for _ in range(n)]  # [maxVal, prevIdx]
        max_val = 0
        max_idx = 0

        def checkWords(i1: int, i2: int) -> bool:
            if groups[i1] == groups[i2]:
                return False
            s1, s2 = words[i1], words[i2]
            if len(s1) != len(s2):
                return False
            dist = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    dist += 1
            return dist == 1

        for i in range(1, n):
            maxVal = 1
            prevIdx = -1
            for j in range(0, i):
                if not checkWords(i, j):
                    continue
                withPrev = dp[j][0] + 1
                if withPrev > maxVal:
                    maxVal = withPrev
                    prevIdx = j
            dp[i] = [maxVal, prevIdx]
            if maxVal > max_val:
                max_val = maxVal
                max_idx = i

        cur = max_idx
        ans = []
        while cur >= 0:
            ans.append(words[cur])
            cur = dp[cur][1]

        return list(reversed(ans))


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 811ms Beats 65.91%
    Memory 18.06MB Beats 88.64%
    """

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = [1] * n
        prev_ = [-1] * n
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if (
                    self.check(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev_[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        ans = []
        i = max_index
        while i >= 0:
            ans.append(words[i])
            i = prev_[i]
        ans.reverse()
        return ans

    def check(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1
