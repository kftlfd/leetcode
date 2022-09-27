"""
Leetcode
838. Push Dominoes (medium)
2022-09-27

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

 - dominoes[i] = 'L', if the ith domino has been pushed to the left,
 - dominoes[i] = 'R', if the ith domino has been pushed to the right, and
 - dominoes[i] = '.', if the ith domino has not been pushed.

Return a string representing the final state.

Example 1:
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
"""


# leetcode solution - Approach #2: Calculate Force
# Runtime: 918 ms, faster than 25.48% of Python3 online submissions for Push Dominoes.
# Memory Usage: 19.3 MB, less than 41.59% of Python3 online submissions for Push Dominoes.
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        force = [0] * N

        # Populate forces going from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f

        # Populate forces going from right to left
        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f == 0 else 'R' if f > 0 else 'L' for f in force)


s = Solution()
tests = [
    "RR.L",
    ".L.R...LR..L..",
]
for t in tests:
    print(t)
    print(s.pushDominoes(t))
    print()
