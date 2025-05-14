"""
Leetcode
2025-05-14
3337. Total Characters in String After Transformations II
Hard
Topics
Companies
Hint

You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

    Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
    The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".

Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

Output: 7

Explanation:

    First Transformation (t = 1):
        'a' becomes 'b' as nums[0] == 1
        'b' becomes 'c' as nums[1] == 1
        'c' becomes 'd' as nums[2] == 1
        'y' becomes 'z' as nums[24] == 1
        'y' becomes 'z' as nums[24] == 1
        String after the first transformation: "bcdzz"

    Second Transformation (t = 2):
        'b' becomes 'c' as nums[1] == 1
        'c' becomes 'd' as nums[2] == 1
        'd' becomes 'e' as nums[3] == 1
        'z' becomes 'ab' as nums[25] == 2
        'z' becomes 'ab' as nums[25] == 2
        String after the second transformation: "cdeabab"

    Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:

Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

Output: 8

Explanation:

    First Transformation (t = 1):
        'a' becomes 'bc' as nums[0] == 2
        'z' becomes 'ab' as nums[25] == 2
        'b' becomes 'cd' as nums[1] == 2
        'k' becomes 'lm' as nums[10] == 2
        String after the first transformation: "bcabcdlm"

    Final Length of the string: The string is "bcabcdlm", which has 8 characters.

 

Constraints:

    1 <= s.length <= 10^5
    s consists only of lowercase English letters.
    1 <= t <= 10^9
    nums.length == 26
    1 <= nums[i] <= 25


Hint 1
Model the problem as a matrix multiplication problem.
Hint 2
Use exponentiation to quickly multiply matrices.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        arr = [0] * 26
        cnt = arr[:]
        a = ord("a")
        for c in s:
            cnt[ord(c) - a] += 1

        for _ in range(t):
            nxt_cnt = arr[:]
            for i, (c, nxt) in enumerate(zip(cnt, nums)):
                if c < 1:
                    continue
                for j in range(i + 1, i + nxt + 1):
                    nxt_cnt[j % 26] += c
            cnt[:] = nxt_cnt

        return sum(cnt) % (10**9 + 7)


class Solution1:
    """
    leetcode solution: Matrix Multiplication + Matrix Exponentiation By Squaring
    Runtime 5694ms Beats 5.68%
    Memory 18.82MB Beats 70.45%
    """

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        L = 26

        class Mat:
            def __init__(self, copy_from: "Mat" = None) -> None:
                self.a: List[List[int]] = [[0] * L for _ in range(L)]
                if copy_from:
                    for i in range(L):
                        for j in range(L):
                            self.a[i][j] = copy_from.a[i][j]

            def __mul__(self, other: "Mat") -> "Mat":
                result = Mat()
                for i in range(L):
                    for j in range(L):
                        for k in range(L):
                            result.a[i][j] = (
                                result.a[i][j] + self.a[i][k] * other.a[k][j]
                            ) % MOD
                return result

        # identity matrix
        def I() -> Mat:
            m = Mat()
            for i in range(L):
                m.a[i][i] = 1
            return m

        # matrix exponentiation by squaring
        def quickmul(x: Mat, y: int) -> Mat:
            ans = I()
            cur = x
            while y:
                if y & 1:
                    ans = ans * cur
                cur = cur * cur
                y >>= 1
            return ans

        T = Mat()
        for i in range(26):
            for j in range(1, nums[i] + 1):
                T.a[(i + j) % 26][i] = 1

        res = quickmul(T, t)

        f = [0] * 26
        for ch in s:
            f[ord(ch) - ord("a")] += 1

        ans = 0
        for i in range(26):
            for j in range(26):
                ans = (ans + res.a[i][j] * f[j]) % MOD

        return ans
