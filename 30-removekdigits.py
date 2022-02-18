'''
Leetcode
402. Remove K Digits (medium)
2022-02-18

Given string num representing a non-negative integer num, and an 
integer k, return the smallest possible integer after removing k 
digits from num.
'''



# taken from
# https://leetcode.com/problems/remove-k-digits/discuss/700059/Python-Very-detail-explanation-with-examples-using-stack/1272182
# Runtime: 58 ms, faster than 51.37% of Python3 online submissions for Remove K Digits.
# Memory Usage: 14.1 MB, less than 81.82% of Python3 online submissions for Remove K Digits.
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num) <= k: return "0"
        
        # stack is mono-stack of increasing digits in num,
        # removing k digits which are bigger than the digit next to it
        stack = []
        for n in num:
            
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1
                
            if stack or n != "0":
                stack.append(n)
             
        # if left with only increasing digits, but still have some
        # available to remove, then remove biggest (from the end)
        if k:
            stack = stack[:-k]
            
        if not stack:
            return "0"
        return "".join(stack)



tests = [
    ["1432219", 3],
    ["10200", 1],
    ["10", 2]
]
solution = Solution()
for test in tests:
    print('test: ', *test)
    print('out:  ', solution.removeKdigits(test[0], test[1]), '\n')