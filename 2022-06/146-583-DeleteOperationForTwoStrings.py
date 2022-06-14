"""
Leetcode
583. Delete Operation for Two Strings (medium)
2022-06-14

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
"""



# leetcode solution
# Runtime: 431 ms, faster than 39.76% of Python3 online submissions for Delete Operation for Two Strings.
# Memory Usage: 17.8 MB, less than 44.69% of Python3 online submissions for Delete Operation for Two Strings.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[len(word1)][len(word2)]



s = Solution()
tests = [
    ["leetcode", "etco"],
    ["sea", "eat"],
]
for t in tests:
    print(t)
    print(s.minDistance(t[0], t[1]))
    print()
