"""
Leetcode
991. Broken Calculator (medium)
2022-03-23

There is a broken calculator that has the integer startValue on its 
display initially. In one operation, you can:

 - multiply the number on display by 2, or
 - subtract 1 from the number on display.

Given two integers startValue and target, return the minimum number 
of operations needed to display target on the calculator.
"""



# leetcode solution + @lee215
# https://leetcode.com/problems/broken-calculator/solution/
# https://leetcode.com/problems/broken-calculator/discuss/234484/JavaC++Python-Change-Y-to-X-in-1-Line
# Runtime: 53 ms, faster than 26.03% of Python3 online submissions for Broken Calculator.
# Memory Usage: 13.9 MB, less than 73.06% of Python3 online submissions for Broken Calculator.
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        res = 0
        
        while target > startValue:
            if target % 2: # if odd: add 1 and divide by 2
                target = (target + 1) // 2
                res += 2
            else: # if even: divide by 2
                target //= 2
                res += 1
                
        return res + (startValue - target) # target is less or equal to sV, add up by 1



s = Solution()
tests = [
    [2, 3],
    [5, 8],
    [3, 10]
]
for t in tests:
    print(t)
    print(s.brokenCalc(t[0], t[1]))
    print()
