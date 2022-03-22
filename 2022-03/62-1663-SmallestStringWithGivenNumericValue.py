"""
Leetcode
1663. Smallest String With A Given Numeric Value (medium)
2022-03-22

The numeric value of a lowercase character is defined as its position 
(1-indexed) in the alphabet, so the numeric value of a is 1, the numeric 
value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is 
defined as the sum of its characters' numeric values. For example, the 
numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest 
string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes 
before y in dictionary order, that is, either x is a prefix of y, or if i 
is the first position such that x[i] != y[i], then x[i] comes before y[i] 
in alphabetic order.
"""



# try 1
# Runtime: 924 ms, faster than 43.78% of Python3 online submissions for Smallest String With A Given Numeric Value.
# Memory Usage: 16 MB, less than 23.96% of Python3 online submissions for Smallest String With A Given Numeric Value.
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        s = []
        
        # stack up maximum values
        for i in range(k // 26):
            s.append(26)
        if k % 26 != 0:
            s.append(k % 26)

        # pad with min values (substracting from the end)
        to_pad = n - len(s)
        i = len(s) - 1 # last element
        while to_pad:
            if s[i] <= 1:
                i -= 1
            else:
                s[i] -= 1
                to_pad -= 1
                s.append(1)

        # convert to letters
        for i in range(len(s)):
            s[i] = chr(s[i] + ord('a') - 1)
        s.reverse()
        
        return ''.join(s)



# try 2
# inspired by @artod
# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/discuss/1871793/Python3-GREEDY-FILLING-()-Explained
# Runtime: 220 ms, faster than 79.72% of Python3 online submissions for Smallest String With A Given Numeric Value.
# Memory Usage: 15.3 MB, less than 68.20% of Python3 online submissions for Smallest String With A Given Numeric Value.
class Solution1:
    def getSmallestString(self, n: int, k: int) -> str:
        
        v = k - n # value left to distibute
        i = n - 1 # starting from last index in s

        # fill a's
        s = ['a'] * n

        # fill z's
        # array is filled with a's (1), so we can add to each index 25
        for _ in range(v // 25): 
            s[i] = 'z'
            i -= 1

        # insert remainder    
        if v % 25 != 0:
            s[i] = chr((v % 25) + ord('a'))
        
        return ''.join(s)


s = Solution1()
tests = [
    [3,27],
    [5,73],
    [3,26*3],
    [1,26],
    [4,4],
    [10,10],
    [10,112]
]
for t in tests:
    print(t)
    print(s.getSmallestString(t[0], t[1]))
    print()
