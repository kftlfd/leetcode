"""
Leetcode
633. Sum of Square Numbers
Medium
2024-06-17

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false



Constraints:

    0 <= c <= 2^31 - 1
"""


from math import sqrt


class Solution3:
    """
    leetcode solution 3: using sqrt function
    Runtime: 144 ms, faster than 18.72% of Python3 online submissions for Sum of Square Numbers.
    Memory Usage: 16.5 MB, less than 39.36% of Python3 online submissions for Sum of Square Numbers.
    """

    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a**2 <= c:
            b = sqrt(c - a**2)
            if b - int(b) == 0:
                return True
            a += 1
        return False


class Solution4:
    """
    leetcode solution 4: binary search
    wrong answer
    """

    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a**2 <= c:
            b = sqrt(c - a**2)
            if self.bin_search(0, b, b):
                return True
            a += 1
        return False

    def bin_search(self, s, e, n) -> bool:
        if s > e:
            return False
        mid = s + (e - s) // 2
        mid_2 = mid**2
        if mid_2 == n:
            return True
        if mid_2 > n:
            return self.bin_search(s, mid - 1, n)
        return self.bin_search(mid + 1, e, n)


class Solution5:
    """
    leetcode solution 5: Fermat theorem
    Runtime: 41 ms, faster than 99.68% of Python3 online submissions for Sum of Square Numbers.
    Memory Usage: 16.5 MB, less than 39.36% of Python3 online submissions for Sum of Square Numbers.
    """

    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while i*i <= c:
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c //= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
            i += 1
        return c % 4 != 3
