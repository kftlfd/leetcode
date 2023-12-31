"""
Leetcode
1220. Count Vowels Permutation (hard)
2022-08-07

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

 - Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
 - Each vowel 'a' may only be followed by an 'e'.
 - Each vowel 'e' may only be followed by an 'a' or an 'i'.
 - Each vowel 'i' may not be followed by another 'i'.
 - Each vowel 'o' may only be followed by an 'i' or a 'u'.
 - Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3: 
Input: n = 5
Output: 68
"""


# Memory Limit Exceeded
class Solution:
    def countVowelPermutation(self, n: int) -> int:

        next = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        q = ['a', 'e', 'i', 'o', 'u']

        for i in range(1, n):
            q2 = []
            for c in q:
                q2 += next[c]
            q = q2

        return len(q) % (10**9 + 7)


# Wrong Answer (?)
# https://leetcode.com/problems/count-vowels-permutation/discuss/2390159/Simple-and-Short-Solution
class Solution1:
    def countVowelPermutation(self, n: int) -> int:

        # No. of one digit strings that ends with vowel
        a = 1
        e = 1
        i = 1
        o = 1
        u = 1

        for i in range(1, n):
            # No. of strings to which vowel can be appended
            a2 = (e + i + u)
            e2 = (a + i)
            i2 = (e + o)
            o2 = (i)
            u2 = (o + i)

            a = a2
            e = e2
            i = i2
            o = o2
            u = u2

        return (a + e + i + o + u) % (10**9 + 7)


# https://leetcode.com/problems/count-vowels-permutation/discuss/2392315/Python-oror-O(n)-TC-O(1)-SC-oror-faster-than-99
# Runtime: 138 ms, faster than 95.58% of Python3 online submissions for Count Vowels Permutation.
# Memory Usage: 13.8 MB, less than 99.08% of Python3 online submissions for Count Vowels Permutation.
class Solution2:
    def countVowelPermutation(self, n: int) -> int:
        a = 1
        e = 1
        i = 1
        o = 1
        u = 1
        BIG_VAL = 1000000007

        n -= 1

        while n:
            new_a = e
            new_e = (a + i) % BIG_VAL
            new_i = (a + e + o + u) % BIG_VAL
            new_o = (i + u) % BIG_VAL
            new_u = a

            a = new_a
            e = new_e
            i = new_i
            o = new_o
            u = new_u

            n -= 1

        return (a + e + i + o + u) % BIG_VAL


s = Solution2()
tests = [
    1, 2, 5, 10,
    (2 * 10**4)
]
for t in tests:
    print(t)
    print(s.countVowelPermutation(t))
    print()
