"""
Leetcode
1220. Count Vowels Permutation (hard)
2023-10-28

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    Each vowel 'a' may only be followed by an 'e'.
    Each vowel 'e' may only be followed by an 'a' or an 'i'.
    Each vowel 'i' may not be followed by another 'i'.
    Each vowel 'o' may only be followed by an 'i' or a 'u'.
    Each vowel 'u' may only be followed by an 'a'.

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

 

Constraints:

    1 <= n <= 2 * 10^4
"""


class Solution:
    """
    Runtime: 484 ms, faster than 36.66% of Python3 online submissions for Count Vowels Permutation.
    Memory Usage: 16.4 MB, less than 77.64% of Python3 online submissions for Count Vowels Permutation.
    """

    def countVowelPermutation(self, n: int) -> int:
        dp = [1] * 5

        for _ in range(2, n + 1):
            nxt_dp = [0] * 5

            for i, c_num in enumerate(dp):
                if i == 0:
                    nxt_dp[1] += c_num
                elif i == 1:
                    nxt_dp[0] += c_num
                    nxt_dp[2] += c_num
                elif i == 2:
                    nxt_dp[0] += c_num
                    nxt_dp[1] += c_num
                    nxt_dp[3] += c_num
                    nxt_dp[4] += c_num
                elif i == 3:
                    nxt_dp[2] += c_num
                    nxt_dp[4] += c_num
                elif i == 4:
                    nxt_dp[0] += c_num

            dp = nxt_dp

        return sum(dp) % (10**9 + 7)


class Solution1:
    """
    Runtime: 231 ms, faster than 56.25% of Python3 online submissions for Count Vowels Permutation.
    Memory Usage: 16.3 MB, less than 77.64% of Python3 online submissions for Count Vowels Permutation.
    """

    def countVowelPermutation(self, n: int) -> int:
        dp = [1] * 5
        a = 0
        e = 1
        i = 2
        o = 3
        u = 4

        for _ in range(2, n + 1):
            nxt = [0] * 5

            nxt[a] = dp[e] + dp[i] + dp[u]
            nxt[e] = dp[a] + dp[i]
            nxt[i] = dp[e] + dp[o]
            nxt[o] = dp[i]
            nxt[u] = dp[i] + dp[o]

            dp = nxt

        return sum(dp) % (10**9 + 7)


s = Solution1()
tests = [
    (1,
     5),

    (2,
     10),

    (5,
     68),
]
for inp, exp in tests:
    res = s.countVowelPermutation(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
