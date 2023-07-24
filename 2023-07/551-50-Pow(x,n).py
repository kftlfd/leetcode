"""
Leetcode
50. Pow(x, n) (medium)
2023-07-24

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Constraints:

    -100.0 < x < 100.0
    -2^31 <= n <= 2^31-1
    n is an integer.
    Either x is not zero or n > 0.
    -10^4 <= xn <= 10^4
"""


class Solution:
    """
    Runtime Error: max recursion depth exceeded
    """

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        return x * self.myPow(x, n-1)


class Solution1:
    """
    Time Limit Exceeded
    """

    def myPow(self, x: float, n: int) -> float:
        ans = 1
        for _ in range(abs(n)):
            ans *= x
        return 1 / ans if n < 0 else ans


class Solution2:
    """
    leetcode solution 1: binary exponentiation (recursive)
    Time: O(log(n))
    Space: O(log(n))
    Runtime: 50 ms, faster than 36.55% of Python3 online submissions for Pow(x, n).
    Memory Usage: 16.3 MB, less than 41.10% of Python3 online submissions for Pow(x, n).
    """

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1.0 / self.myPow(x, -n)

        # perform binary exponentiation
        # if n is odd we perform binary exponentiation on n-1 and multipy with x
        if n % 2 == 1:
            return x * self.myPow(x * x, (n - 1) // 2)

        # otherwise we calculate binary exponentiation on n
        return self.myPow(x * x, n // 2)


class Solution3:
    """
    leetcode solution 2: binary exponentiation (iterative)
    Time: O(log(n))
    Space: O(1)
    Runtime: 51 ms, faster than 31.80% of Python3 online submissions for Pow(x, n).
    Memory Usage: 16.3 MB, less than 41.10% of Python3 online submissions for Pow(x, n).
    """

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n = -1 * n
            x = 1.0 / x

        # Perform Binary Exponentiation.
        result = 1
        while n != 0:
            # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
            if n % 2 == 1:
                result *= x
                n -= 1
            # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
            x *= x
            n //= 2
        return result


class Solution4:
    """
    python built-in
    Runtime: 56 ms, faster than 7.93% of Python3 online submissions for Pow(x, n).
    Memory Usage: 16.2 MB, less than 78.07% of Python3 online submissions for Pow(x, n).
    """

    def myPow(self, x: float, n: int) -> float:
        return x**n


s = Solution()
tests = [
    ((2.0, 10),
     1024.0),

    ((2.1, 3),
     9.261),

    ((2.0, -2),
     0.25),
]
for inp, exp in tests:
    res = s.myPow(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
