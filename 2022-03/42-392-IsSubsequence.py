'''
Leetcode
392. Is Subsequence (easy)
2022-03-02

Given two strings s and t, return true if s is a subsequence of t, or 
false otherwise.

A subsequence of a string is a new string that is formed from the 
original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''



# try 1
# Runtime: 45 ms, faster than 56.23% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14 MB, less than 73.22% of Python3 online submissions for Is Subsequence.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) < 1:
            return True
        
        # pointer (index)
        p = 0
        for i in range(len(t)):
            if s[p] == t[i]:
                p += 1
            if p == len(s):
                return True

        return False



# https://leetcode.com/problems/is-subsequence/discuss/87258/2-lines-Python
# Runtime: 32 ms, faster than 89.80% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14 MB, less than 73.22% of Python3 online submissions for Is Subsequence.
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)



tests = [
    ["abc", "ahbgdc"],
    ["axc", "ahbgdc"],
    ["", "ahbgdc"],
    ["ahbgdc", ""],
    ["b", "abc"]
]
s = Solution2()
for test in tests:
    print(test)
    print("-->", s.isSubsequence(test[0], test[1]), "\n")