"""
Leetcode
1318. Minimum Flips to Make a OR b Equal to c (medium)
2023-06-07

Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

Example 1:

Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:

Input: a = 4, b = 2, c = 7
Output: 1

Example 3:

Input: a = 1, b = 2, c = 3
Output: 0

Constraints:

    1 <= a <= 10^9
    1 <= b <= 10^9
    1 <= c <= 10^9
"""


class Solution:
    """
    Runtime: 43 ms, faster than 68.57% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
    Memory Usage: 16.4 MB, less than 25.27% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
    """

    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        for a, b, c in zip(f"{a:030b}", f"{b:030b}", f"{c:030b}"):
            if c == "0":
                flips += (a == "1") + (b == "1")

            else:  # c == "1"
                flips += (a != "1" and b != "1")

        return flips


class Solution1:
    """
    leetcode solution 1: Bit Manipulation
    Runtime: 52 ms, faster than 15.38% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
    Memory Usage: 16.4 MB, less than 25.27% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
    """

    def minFlips(self, a: int, b: int, c: int) -> int:
        answer = 0

        while a or b or c:
            if c & 1:
                answer += 0 if ((a & 1) or (b & 1)) else 1
            else:
                answer += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1

        return answer


class Solution2:
    """
    leetcode solution 2: Count the Number of Set Bits Using Built-in Function
    Runtime: 56 ms, faster than 6.59% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
    Memory Usage: 16.4 MB, less than 25.27% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
    """

    def minFlips(self, a: int, b: int, c: int) -> int:
        # In 3.9 or earlier
        # return bin((a | b) ^ c).count("1") + bin(a & b & ((a | b) ^ c)).count("1")

        # In 3.10 or later
        return ((a | b) ^ c).bit_count() + (a & b & ((a | b) ^ c)).bit_count()


s = Solution()
tests = [
    ((2, 6, 5),
     3),

    ((4, 2, 7),
     1),

    ((1, 2, 3),
     0),
]
for inp, exp in tests:
    res = s.minFlips(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
