"""
Leetcode
12. Integer to Roman (medium)
2022-10-20

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

 - I can be placed before V (5) and X (10) to make 4 and 9. 
 - X can be placed before L (50) and C (100) to make 40 and 90. 
 - C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

from typing import List, Optional


# Runtime: 104 ms, faster than 38.30% of Python3 online submissions for Integer to Roman.
# Memory Usage: 13.9 MB, less than 35.57% of Python3 online submissions for Integer to Roman.
class Solution:
    romnums = {
        1: {
            "0": "",
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX"
        },


        2: {
            "0": "",
            "1": "X",
            "2": "XX",
            "3": "XXX",
            "4": "XL",
            "5": "L",
            "6": "LX",
            "7": "LXX",
            "8": "LXXX",
            "9": "XC"
        },

        3: {
            "0": "",
            "1": "C",
            "2": "CC",
            "3": "CCC",
            "4": "CD",
            "5": "D",
            "6": "DC",
            "7": "DCC",
            "8": "DCCC",
            "9": "CM"
        },

        4: {
            "0": "",
            "1": "M",
            "2": "MM",
            "3": "MMM",
        }
    }

    def intToRoman(self, num: int) -> str:
        ans = []
        for i, d in enumerate(str(num)[::-1]):
            ans.insert(0, self.romnums[i+1][d])
        return "".join(ans)


s = Solution()
tests = [
    (3,
     'III'),

    (58,
     'LVIII'),

    (1994,
     'MCMXCIV'),

    (10,
     'X'),
]
for inp, exp in tests:
    res = s.intToRoman(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
print('Completed testing')
