"""
Leetcode
319. Bulb Switcher (medium)
2023-04-27

There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

Example 1:
Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 1
"""

from math import floor, sqrt


class Solution1:
    """
    https://www.youtube.com/watch?v=-UBDRX6bk-A
    Runtime: 42 ms, faster than 8.42% of Python3 online submissions for Bulb Switcher.
    Memory Usage: 16.3 MB, less than 34.09% of Python3 online submissions for Bulb Switcher.
    """

    def bulbSwitch(self, n: int) -> int:
        return floor(n**0.5)


class Solution2:
    """
    leetcode solution
    Runtime: 50 ms, faster than 8.42% of Python3 online submissions for Bulb Switcher.
    Memory Usage: 16.3 MB, less than 34.09% of Python3 online submissions for Bulb Switcher.
    """

    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))


s = Solution1()
tests = [
    (3, 1),
    (0, 0),
    (1, 1),
    (100, 10),
]
for inp, exp in tests:
    res = s.bulbSwitch(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
