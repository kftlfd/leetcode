"""
Leetcode
680. Valid Palindrome II (easy)
2022-04-02

Given a string s, return true if the s can be palindrome 
after deleting at most one character from it.
"""



# try 1
# wrong
class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        removed = False
        while start < end:
            if s[start] != s[end]:
                if removed: return False
                removed = True
                if s[start] == s[end-1]:
                    end -= 1
                else:
                    start += 1
            else:
                start += 1
                end -= 1
        return True



# leetcode solution
# Runtime: 233 ms, faster than 32.89% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 14.4 MB, less than 91.68% of Python3 online submissions for Valid Palindrome II.
class Solution1:
    def validPalindrome(self, s: str) -> bool:
        
        def check(s, i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True

        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return check(s, start+1, end) or check(s, start, end-1)
            start += 1
            end -= 1
        return True



s = Solution()
tests = [
    "aba",
    "abca",
    "abc",
    "ebcbbececabbacecbbcbe"
]
for t in tests:
    print(t)
    print(s.validPalindrome(t))
    print()
