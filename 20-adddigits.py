'''
Leetcode
258. Add Digits (easy)
2022-02-08

Given an integer num, repeatedly add all its digits 
until the result has only one digit, and return it.
https://leetcode.com/problems/add-digits/
'''



# Try 1
# Runtime: 40 ms, faster than 51.49% of Python3 online submissions for Add Digits.
# Memory Usage: 13.8 MB, less than 91.66% of Python3 online submissions for Add Digits.
class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s) > 1:
            s = str(sum(int(digit) for digit in s))
        return int(s)



# Leetcode solution
# O(1)
# Runtime: 51 ms, faster than 31.87% of Python3 online submissions for Add Digits.
# Memory Usage: 13.8 MB, less than 91.66% of Python3 online submissions for Add Digits.
class Solution2:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0