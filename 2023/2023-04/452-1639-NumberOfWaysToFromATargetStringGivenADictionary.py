"""
Leetcode
1639. Number of Ways to Form a Target String Given a Dictionary (hard)
2023-04-16

You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

    target should be formed from left to right.
    To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
    Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
    Repeat the process until you form the string target.

Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

Example 1:
Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

Example 2:
Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: Bottom-up Dynamic Programming
    Runtime: 3757 ms, faster than 9.73% of Python3 online submissions for Number of Ways to Form a Target String Given a Dictionary.
    Memory Usage: 38.9 MB, less than 73.93% of Python3 online submissions for Number of Ways to Form a Target String Given a Dictionary.
    """

    def numWays(self, words: List[str], target: str) -> int:
        alphabet = 26
        mod = 1000000007
        m = len(target)
        k = len(words[0])
        cnt = [[0] * k for _ in range(alphabet)]
        for j in range(k):
            for word in words:
                cnt[ord(word[j]) - ord('a')][j] += 1
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(m + 1):
            for j in range(k):
                if i < m:
                    dp[i + 1][j +
                              1] += (cnt[ord(target[i]) - ord('a')][j] * dp[i][j])
                    dp[i + 1][j + 1] %= mod
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= mod
        return dp[m][k]


class Solution2:
    """
    leetcode solution 2: Top-Down Dynamic Programming (Memoization)
    Runtime: 2472 ms, faster than 49.03% of Python3 online submissions for Number of Ways to Form a Target String Given a Dictionary.
    Memory Usage: 45.1 MB, less than 62.26% of Python3 online submissions for Number of Ways to Form a Target String Given a Dictionary.
    """

    def numWays(self, words: List[str], target: str) -> int:
        alphabet = 26
        mod = 1000000007
        m = len(target)
        k = len(words[0])
        cnt = [[0] * k for _ in range(alphabet)]
        for j in range(k):
            for word in words:
                cnt[ord(word[j]) - ord('a')][j] += 1
        dp = [[-1] * (k + 1) for _ in range(m + 1)]

        def f(i, j):
            if j == 0:
                return 1 if i == 0 else 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = f(i, j - 1)
            if i > 0:
                dp[i][j] += (cnt[ord(target[i - 1]) - ord('a')][j - 1]
                             * f(i - 1, j - 1))
            dp[i][j] %= mod
            return dp[i][j]

        return f(m, k)


s = Solution2()
tests = [
    ((["acca", "bbbb", "caca"], "aba"),
     6),

    ((["abba", "baab"], "bab"),
     4),
]
for inp, exp in tests:
    res = s.numWays(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
