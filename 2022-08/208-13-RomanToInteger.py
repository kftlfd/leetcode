"""
Leetcode
13. Roman to Integer (easy)
2022-08-15

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

 - I can be placed before V (5) and X (10) to make 4 and 9. 
 - X can be placed before L (50) and C (100) to make 40 and 90. 
 - C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


# Runtime: 50 ms, faster than 92.41% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.9 MB, less than 31.19% of Python3 online submissions for Roman to Integer.
class Solution:
    def romanToInt(self, s: str) -> int:

        out = 0
        chars = '0' + s

        for i in range(len(chars)):

            if chars[i] == 'I':
                out += 1

            elif chars[i] == 'V':
                if chars[i-1] == 'I':
                    out += 3
                else:
                    out += 5

            elif chars[i] == 'X':
                if chars[i-1] == 'I':
                    out += 8
                else:
                    out += 10

            elif chars[i] == 'L':
                if chars[i-1] == 'X':
                    out += 30
                else:
                    out += 50

            elif chars[i] == 'C':
                if chars[i-1] == 'X':
                    out += 80
                else:
                    out += 100

            elif chars[i] == 'D':
                if chars[i-1] == 'C':
                    out += 300
                else:
                    out += 500

            elif chars[i] == 'M':
                if chars[i-1] == 'C':
                    out += 800
                else:
                    out += 1000

        return out


s = Solution()
tests = [
    "III",
    "LVIII",
    "MCMXCIV",
]
for t in tests:
    print(t)
    print(s.romanToInt(t))
    print()
