"""
Leetcode
509. Fibonacci Number (easy)
2022-07-06

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
"""


# recursion
# Runtime: 1407 ms, faster than 6.40% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 9.50% of Python3 online submissions for Fibonacci Number.
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)


# recursion with memoization
# Runtime: 67 ms, faster than 32.13% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 9.50% of Python3 online submissions for Fibonacci Number.
class Solution1:
    memo = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
            return self.memo[n]


# iterative with memoization
# Runtime: 47 ms, faster than 60.27% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 9.50% of Python3 online submissions for Fibonacci Number.
class Solution2:
    memo = {0: 0, 1: 1}
    last = 1

    def fib(self, n: int) -> int:
        if n <= self.last:
            return self.memo[n]

        curr = self.last + 1
        while curr <= n:
            self.memo[curr] = self.memo[curr-1] + self.memo[curr-2]
            curr += 1

        self.last = n

        return self.memo[n]


# https://leetcode.com/problems/fibonacci-number/discuss/217637/Python-100-iterative
# Runtime: 26 ms, faster than 98.16% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 9.50% of Python3 online submissions for Fibonacci Number.
class Solution3:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a+b
        return a


s = Solution2()
tests = [
    2,
    3,
    4,
    10,
    30,
    60
]
for t in tests:
    print(t)
    print(s.fib(t))
    print()
