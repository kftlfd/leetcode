"""
Leetcode
374. Guess Number Higher or Lower (easy)
2022-11-16

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

 - -1: Your guess is higher than the number I picked (i.e. num > pick).
 - 1: Your guess is lower than the number I picked (i.e. num < pick).
 - 0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


from typing import List, Optional


# Runtime: 54 ms, faster than 53.16% of Python3 online submissions for Guess Number Higher or Lower.
# Memory Usage: 13.9 MB, less than 15.89% of Python3 online submissions for Guess Number Higher or Lower.
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            m = (l + r) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == 1:
                l = m + 1
            elif res == -1:
                r = m - 1


def guess(n: int) -> int:
    if n == pick:
        return 0
    if n > pick:
        return -1
    return 1


s = Solution()
tests = [
    ((10, 6),
     6),

    ((1, 1),
     1),

    ((2, 1),
     1),
]
for inp, exp in tests:
    n, pick = inp
    res = s.guessNumber(n)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
