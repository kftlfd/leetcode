"""
Leetcode
2026-04-12
1320. Minimum Distance to Type a Word Using Two Fingers
Hard

You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

    For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).

Given the string word, return the minimum total distance to type such string using only two fingers.

The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

 

Example 1:

Input: word = "CAKE"
Output: 3
Explanation: Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3

Example 2:

Input: word = "HAPPY"
Output: 6
Explanation: Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6

 

Constraints:

    2 <= word.length <= 300
    word consists of uppercase English letters.


Hint 1
Use dynamic programming.
Hint 2
dp[i][j][k]: smallest movements when you have one finger on i-th char and the other one on j-th char already having written k first characters from word.
"""


class Solution1:
    """
    leetcode solution 1: Dynamic Programming
    Runtime 122ms Beats 70.72%
    Memory 21.70MB Beats 65.19%
    """

    def minimumDistance(self, word: str) -> int:
        n = len(word)
        BIG = 2**30
        dp = [[[BIG] * 26 for x in range(26)] for y in range(n)]
        for i in range(26):
            dp[0][i][ord(word[0]) - 65] = 0
            dp[0][ord(word[0]) - 65][i] = 0

        def getDistance(p, q):
            x1, y1 = p // 6, p % 6
            x2, y2 = q // 6, q % 6
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(1, n):
            cur, prev = ord(word[i]) - 65, ord(word[i - 1]) - 65
            d = getDistance(prev, cur)
            for j in range(26):
                dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][prev][j] + d)
                dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][prev] + d)
                if prev == j:
                    for k in range(26):
                        d0 = getDistance(k, cur)
                        dp[i][cur][j] = min(
                            dp[i][cur][j], dp[i - 1][k][j] + d0)
                        dp[i][j][cur] = min(
                            dp[i][j][cur], dp[i - 1][j][k] + d0)

        ans = min(min(dp[n - 1][x]) for x in range(26))
        return ans


class Solution2:
    """
    leetcode solution 2: Dynamic Programming + Space Optimization
    Runtime 45ms Beats 93.37%
    Memory 19.48MB Beats 79.01%
    """

    def minimumDistance(self, word: str) -> int:
        n = len(word)
        BIG = 2**30
        dp = [[0] * 26] + [[BIG] * 26 for _ in range(n - 1)]

        def getDistance(p, q):
            x1, y1 = p // 6, p % 6
            x2, y2 = q // 6, q % 6
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(1, n):
            cur, prev = ord(word[i]) - 65, ord(word[i - 1]) - 65
            d = getDistance(prev, cur)
            for j in range(26):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + d)
                if prev == j:
                    for k in range(26):
                        d0 = getDistance(k, cur)
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + d0)

        ans = min(dp[n - 1])
        return ans
