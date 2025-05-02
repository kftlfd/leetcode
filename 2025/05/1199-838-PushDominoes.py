"""
Leetcode
2025-05-02
838. Push Dominoes
Solved
Medium
Topics
Companies

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

    dominoes[i] = 'L', if the ith domino has been pushed to the left,
    dominoes[i] = 'R', if the ith domino has been pushed to the right, and
    dominoes[i] = '.', if the ith domino has not been pushed.

Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:

Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

 

Constraints:

    n == dominoes.length
    1 <= n <= 10^5
    dominoes[i] is either 'L', 'R', or '.'.


"""


class Solution:
    """
    Runtime 103ms Beats 84.54%
    Memory 19.37MB Beats 90.46%
    """

    def pushDominoes(self, dominoes: str) -> str:
        ans = list(dominoes)
        n = len(ans)
        i = 0
        left = 0
        push_right_from = None

        while i < n:
            cur = ans[i]

            if cur == "L":
                if push_right_from is not None:
                    r = push_right_from
                    l = i
                    while r < l:
                        ans[r] = "R"
                        ans[l] = "L"
                        r += 1
                        l -= 1
                    push_right_from = None
                else:
                    for j in range(left, i):
                        ans[j] = "L"
                left = i + 1

            elif cur == "R" or i == n - 1:
                if push_right_from is not None:
                    for j in range(push_right_from, i + 1):
                        ans[j] = "R"
                push_right_from = i

            i += 1

        return "".join(ans)


class Solution1:
    """
    leetcode solution 1: Adjacent Symbols
    Runtime 137ms Beats 77.63%
    Memory 27.59MB Beats 9.87%
    """

    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        def cmp(a, b):
            """python2 polyfill"""
            return (a > b) - (a < b)

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y:  # RL
                for k in range(i+1, j):
                    ans[k] = '.LR'[cmp(k-i, j-k)]

        return "".join(ans)


class Solution2:
    """
    leetcode solution 2: Calculate Force
    Runtime 309ms Beats 12.83%
    Memory 23.09MB Beats 42.11%
    """

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

        return "".join('.' if f == 0 else 'R' if f > 0 else 'L'
                       for f in force)


s = Solution()
tests = [
    ("..R..",
     "..RRR"),
]
for inp, exp in tests:
    res = s.pushDominoes(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
