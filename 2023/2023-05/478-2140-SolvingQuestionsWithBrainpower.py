"""
Leetcode
2140. Solving Questions With Brainpower (medium)
2023-05-13

You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

    For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
        If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
        If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.

Return the maximum points you can earn for the exam.

Example 1:
Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

Example 2:
Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def mostPoints(self, questions: List[List[int]]) -> int:

        def dfs(curr_idx):
            if curr_idx >= len(questions):
                return 0

            skip = dfs(curr_idx + 1)

            choose = questions[curr_idx][0] + \
                dfs(curr_idx + questions[curr_idx][1] + 1)

            return max(skip, choose)

        return dfs(0)


class Solution1:
    """
    leetcode solution 1: DP iterative
    Runtime: 1587 ms, faster than 90.91% of Python3 online submissions for Solving Questions With Brainpower.
    Memory Usage: 62.6 MB, less than 55.34% of Python3 online submissions for Solving Questions With Brainpower.
    """

    def mostPoints(self, questions: List[List[int]]) -> int:

        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1):
            dp[i] = questions[i][0]
            skip = questions[i][1]
            if i + skip + 1 < n:
                dp[i] += dp[i + skip + 1]

            dp[i] = max(dp[i], dp[i + 1])

        return dp[0]


class Solution2:
    """
    leetcode solution 2: DP recursive
    Runtime: 1731 ms, faster than 40.71% of Python3 online submissions for Solving Questions With Brainpower.
    Memory Usage: 147.6 MB, less than 40.71% of Python3 online submissions for Solving Questions With Brainpower.
    """

    def mostPoints(self, questions: List[List[int]]) -> int:

        n = len(questions)
        dp = [0] * n

        def dfs(idx):
            if idx >= n:
                return 0

            if dp[idx]:
                return dp[idx]

            points, skip = questions[idx]

            dp[idx] = max(dfs(idx + 1), points + dfs(idx + skip + 1))

            return dp[idx]

        return dfs(0)


s = Solution2()
tests = [
    ([[3, 2], [4, 3], [4, 4], [2, 5]],
     5),

    ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
     7),
]
for inp, exp in tests:
    res = s.mostPoints(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
