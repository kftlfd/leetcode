"""
Leetcode
844. Backspace String Compare (easy)
2022-05-01

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""



# try 1
# Runtime: 34 ms, faster than 77.69% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 13.8 MB, less than 98.80% of Python3 online submissions for Backspace String Compare.
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
                
        def simulate(s):
            out = []
            for c in s:
                if c != '#':
                    out.append(c)
                elif len(out) > 0:
                    out.pop()
            return out
        
        return simulate(s) == simulate(t)



s = Solution()
tests = [
    ["y#fo##f", "y#f#o##f"],
    ["ab#c", "ad#c"],
    ["ab##", "c#d#"],
    ["a#c", "b"]
]
for t in tests:
    print(t)
    print(s.backspaceCompare(t[0], t[1]))
    print()
