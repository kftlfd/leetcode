"""
Leetcode
1444. Number of Ways of Cutting a Pizza (hard)
2023-03-31

Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

Example 2:
Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:
Input: pizza = ["A..","A..","..."], k = 1
Output: 1
"""

from typing import List


class Solution:
    """
    leetcode solution
    Runtime: 209 ms, faster than 75.20% of Python3 online submissions for Number of Ways of Cutting a Pizza.
    Memory Usage: 14.2 MB, less than 96.48% of Python3 online submissions for Number of Ways of Cutting a Pizza.
    """

    def ways(self, pizza: List[str], k: int) -> int:
        rows = len(pizza)
        cols = len(pizza[0])
        apples = [[0] * (cols + 1) for row in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                apples[row][col] = ((pizza[row][col] == 'A')
                                    + apples[row + 1][col]
                                    + apples[row][col + 1]
                                    - apples[row + 1][col + 1])
        f = [[int(apples[row][col] > 0) for col in range(cols)]
             for row in range(rows)]
        mod = 1000000007
        for _ in range(1, k):
            g = [[0 for col in range(cols)] for row in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    for next_row in range(row + 1, rows):
                        if apples[row][col] - apples[next_row][col] > 0:
                            g[row][col] += f[next_row][col]
                    for next_col in range(col + 1, cols):
                        if apples[row][col] - apples[row][next_col] > 0:
                            g[row][col] += f[row][next_col]
                    g[row][col] %= mod
            f = g
        return f[0][0]


s = Solution()
tests = [
    ((["A..", "AAA", "..."], 3),
     3),

    ((["A..", "AA.", "..."], 3),
     1),

    ((["A..", "A..", "..."], 1),
     1),
]
for inp, exp in tests:
    res = s.ways(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
