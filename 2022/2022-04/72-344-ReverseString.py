"""
Leetcode
344. Reverse String (easy)
2022-04-01

Write a function that reverses a string. The input string is given as 
an array of characters s.

You must do this by modifying the input array in-place with O(1) extra 
memory.
"""

from typing import List

"""
Do not return anything, modify s in-place instead.
"""


# try 1
# Runtime: 214 ms, faster than 79.27% of Python3 online submissions for Reverse String.
# Memory Usage: 18.7 MB, less than 15.24% of Python3 online submissions for Reverse String.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]



# Runtime: 341 ms, faster than 22.55% of Python3 online submissions for Reverse String.
# Memory Usage: 18.4 MB, less than 48.50% of Python3 online submissions for Reverse String.
class Solution1:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()



# Runtime: 249 ms, faster than 60.45% of Python3 online submissions for Reverse String.
# Memory Usage: 18.4 MB, less than 48.50% of Python3 online submissions for Reverse String.
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1



s = Solution2()
tests = [
    ["h","e","l","l","o"],
    ["H","a","n","n","a","h"]
]
for t in tests:
    print(t)
    s.reverseString(t)
    print(t)
    print()
