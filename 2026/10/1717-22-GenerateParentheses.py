"""
Leetcode
2026-10-02
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.39MB Beats 74.80%
    """

    def generateParenthesis(self, n: int) -> list[str]:
        ans: list[str] = []

        def generate(cur: str, a: int, b: int):
            if a == 0 and b == 0:
                ans.append(cur)
                return
            if a > 0:
                generate(cur + "(", a - 1, b)
            if b > a:
                generate(cur + ")", a, b - 1)

        generate("", n, n)
        return ans
