"""
Leetcode
5. Longest Palindromic Substring (medium)
2022-06-16

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""



# Time Limit Exceeded
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l = len(s)
        
        # indexes of palindromes: (a,b) => s[a:b+1] is a palindrome
        dp = set()

        # single character substrings
        # (all are palindromes)
        for i in range(l):
            dp.add( (i, i) )

        # double character substrings
        # (palinfrome if both characters are the same)
        for i in range(1, l):
            if s[i-1] == s[i]:
                dp.add( (i-1, i) )

        # rest of substrings - s[i:i+j+1], indexes (i, i+j)
        # cycle through all 3 character substrings, then 4 and so on
        for j in range(2, l):
            for i in range(l-j):
                # if first and last characters in substring (s[i] and s[s+j]) are the same
                # and between them (s[i +1 : i+j -1]) is a palindrome, then it is a palindrome
                if (i +1, i+j -1) in dp and s[i] == s[i+j]:
                    dp.add( (i, i+j) )
        
        # find longest palindrome
        maxlen = 0
        out = None
        for a,b in dp:
            tmp = b - a + 1
            if tmp > maxlen:
                maxlen = tmp
                out = s[a:b+1]

        return out



# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
# Runtime: 1491 ms, faster than 47.35% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14 MB, less than 59.59% of Python3 online submissions for Longest Palindromic Substring.
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        # check for longest palindromes for every index in s
        res = ''
        for i in range(len(s)):
            res = max(
                res,
                self.helperLongestPalindrome(s, i, i), # palindrome of odd length, center is single character
                self.helperLongestPalindrome(s, i, i+1), # even, center is two characters
                key=len
            )
        return res

    def helperLongestPalindrome(self, s, l, r):
        # Return the longest palindrome which center is (l,r)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]



s = Solution1()
tests = [
    "babad",
    "cbbd",
    "fcfcfthnhtfchhhchhh",
]
for t in tests:
    print(t)
    print(s.longestPalindrome(t))
    print()
