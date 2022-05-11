"""
Leetcode
1641. Count Sorted Vowel Strings (medium)
2022-05-11

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045
"""



# try 1 - recursion
# Runtime: 52 ms, faster than 37.74% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 13.9 MB, less than 27.45% of Python3 online submissions for Count Sorted Vowel Strings.
class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        def recursion(n):
            if n == 1:
                return [1, 1, 1, 1, 1]
            else:
                prev = recursion(n - 1)
                return [ sum(prev[0:i]) for i in range(1,6) ]
                
        return sum(recursion(n))



# just loop
# Runtime: 33 ms, faster than 80.43% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 13.8 MB, less than 65.31% of Python3 online submissions for Count Sorted Vowel Strings.
class Solution1:
    def countVowelStrings(self, n: int) -> int:
        i = 1
        nums = [1] * 5
        r = range(1,6)

        while i < n:
            nums = [ sum(nums[0:j]) for j in r ]
            i += 1

        return sum(nums)



# https://leetcode.com/problems/count-sorted-vowel-strings/discuss/918392/Very-Easy-Solution-or-No-DP-or-No-Math-Formula-or-Solving-for-n-3-reveals-the-pattern
# Runtime: 70 ms, faster than 18.30% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 13.9 MB, less than 65.31% of Python3 online submissions for Count Sorted Vowel Strings.
class Solution2:
    def countVowelStrings(self, n: int) -> int:
        ans = 0

        i = 1
        while i <= n + 1:
            sum = 0

            for j in range(1,i+1):
                sum += j
                ans += sum

            i += 1

        return ans



# https://leetcode.com/problems/count-sorted-vowel-strings/discuss/918498/JavaC++Python-DP-O(1)-Time-and-Space
# Runtime: 53 ms, faster than 36.21% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 13.8 MB, less than 65.31% of Python3 online submissions for Count Sorted Vowel Strings.
class Solution3:
    def countVowelStrings(self, n: int) -> int:
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24

        # or
        # return comb(n + 4, 4)
        # Runtime: 39 ms, faster than 64.17% of Python3 online submissions for Count Sorted Vowel Strings.
        # Memory Usage: 13.9 MB, less than 65.31% of Python3 online submissions for Count Sorted Vowel Strings.



s = Solution2()
tests = [1,2,3,4,5,10,33]
for t in tests:
    print(t)
    print(s.countVowelStrings(t))
    print()
