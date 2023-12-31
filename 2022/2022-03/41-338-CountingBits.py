'''
Leetcode
338. Counting Bits (easy)
2022-03-01

Given an integer n, return an array ans of length n + 1 such that 
for each i (0 <= i <= n), ans[i] is the number of 1's in the 
binary representation of i.
'''

from typing import List



# try 1
# Runtime: 159 ms, faster than 34.99% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.8 MB, less than 87.66% of Python3 online submissions for Counting Bits.
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0: return [0]
        
        out = []
        
        for i in range(n + 1):
            out.append(str(bin(i)).count("1"))

        return out



tests = [2,5,64,63]
s = Solution()
for test in tests:
    print(test, "-->", s.countBits(test))