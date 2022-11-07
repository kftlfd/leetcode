"""
Leetcode
1323. Maximum 69 Number (easy)
2022-11-07

You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
"""

from typing import List, Optional


# Runtime: 59 ms, faster than 37.11% of Python3 online submissions for Maximum 69 Number.
# Memory Usage: 13.7 MB, less than 95.47% of Python3 online submissions for Maximum 69 Number.
class Solution:
    def maximum69Number(self, num: int) -> int:
        n = str(num)
        change = -1
        for i in range(len(n)):
            if n[i] == "6":
                change = i
                break
        if change == -1:
            return num
        return int(n[:i] + "9" + n[i+1:])


# Runtime: 26 ms, faster than 98.46% of Python3 online submissions for Maximum 69 Number.
# Memory Usage: 13.8 MB, less than 95.47% of Python3 online submissions for Maximum 69 Number.
class Solution1:
    def maximum69Number(self, num: int) -> int:
        n = str(num)
        return int(n.replace('6', '9', 1))


s = Solution()
tests = [
    (9669,
     9969),

    (9996,
     9999),

    (9999,
     9999),
]
for inp, exp in tests:
    res = s.maximum69Number(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
