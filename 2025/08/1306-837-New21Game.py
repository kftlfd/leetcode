"""
Leetcode
2025-08-17
837. New 21 Game
Medium

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

 

Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.

Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.

Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278

 

Constraints:

    0 <= k <= n <= 10^4
    1 <= maxPts <= 10^4


"""

from collections import deque


class Solution01:
    """
    Memory Limit Exceeded
    """

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        q = deque([(0, 1.0)])  # points, probability
        draw_prob = 1 / maxPts
        ans = 0.0

        while q:
            points, prob = q.popleft()
            for i in range(1, maxPts + 1):
                nxt_points = points + i
                nxt_prob = prob * draw_prob
                if nxt_points >= k:
                    if nxt_points <= n:
                        ans += nxt_prob
                    continue
                q.append((nxt_points, nxt_prob))

        return ans


class Solution1:
    """
    leetcode solution
    Runtime 28ms Beats 32.26%
    Memory 18.27MB Beats 62.26%
    """

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # unoptimized:
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # for i in range(1, n + 1):
        #     for j in range(1, maxPts + 1):
        #         if i - j >= 0 and i - j < k:
        #             dp[i] += dp[i - j] / maxPts
        # return sum(dp[k:])

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        s = 1 if k > 0 else 0
        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]
        return sum(dp[k:])
