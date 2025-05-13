"""
Leetcode
2025-05-13
3335. Total Characters in String After Transformations I
Medium
Topics
Companies
Hint

You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

    If the character is 'z', replace it with the string "ab".
    Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.

Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2

Output: 7

Explanation:

    First Transformation (t = 1):
        'a' becomes 'b'
        'b' becomes 'c'
        'c' becomes 'd'
        'y' becomes 'z'
        'y' becomes 'z'
        String after the first transformation: "bcdzz"
    Second Transformation (t = 2):
        'b' becomes 'c'
        'c' becomes 'd'
        'd' becomes 'e'
        'z' becomes "ab"
        'z' becomes "ab"
        String after the second transformation: "cdeabab"
    Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:

Input: s = "azbk", t = 1

Output: 5

Explanation:

    First Transformation (t = 1):
        'a' becomes 'b'
        'z' becomes "ab"
        'b' becomes 'c'
        'k' becomes 'l'
        String after the first transformation: "babcl"
    Final Length of the string: The string is "babcl", which has 5 characters.

 

Constraints:

    1 <= s.length <= 10^5
    s consists only of lowercase English letters.
    1 <= t <= 10^5


Hint 1
Maintain the frequency of each character.
"""


from collections import Counter


class Solution00:
    """
    Time Limit Exceeded
    """

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = Counter(s)

        for _ in range(t):
            nxt_cnt = Counter()
            for c, n in cnt.items():
                if c == "z":
                    nxt_cnt["a"] += n
                    nxt_cnt["b"] += n
                else:
                    nxt_cnt[chr(ord(c) + 1)] += n
            cnt = nxt_cnt

        return sum(cnt.values()) % (10**9 + 7)


class Solution01:
    """
    Runtime 5213ms Beats 32.03%
    Memory 18.20MB Beats 62.09%
    """

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0] * 26
        a = ord("a")
        for c in s:
            cnt[ord(c) - a] += 1

        for _ in range(t):
            nxt_cnt = [0] * 26
            for i in range(25):
                nxt_cnt[i + 1] += cnt[i]
            nxt_cnt[0] += cnt[-1]
            nxt_cnt[1] += cnt[-1]
            cnt = nxt_cnt

        return sum(cnt) % (10**9 + 7)


class Solution02:
    """
    Runtime 2164ms Beats 64.05%
    Memory 18.08MB Beats 91.50%
    """

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0] * 26
        a = ord("a")
        for c in s:
            cnt[ord(c) - a] += 1

        for _ in range(t):
            z = cnt[-1]
            for i in range(25, 0, -1):
                cnt[i] = cnt[i - 1]
            cnt[0] = z
            cnt[1] += z

        return sum(cnt) % (10**9 + 7)


class Solution1:
    """
    leetcode solution: Recurrence
    Runtime 2206ms Beats 62.74%
    Memory 18.29MB Beats 62.09%
    """

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        for _ in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = (cnt[25] + cnt[0]) % mod
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
        ans = sum(cnt) % mod
        return ans


class Solution2:
    """
    sample 310ms solution
    Runtime 277ms Beats 97.39%
    Memory 22.44MB Beats 24.18%
    """

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        dp = [1] * (t + 26)
        for i in range(26, len(dp)):
            dp[i] = (dp[i-26] + dp[i-25]) % 1_000_000_007
        ans = 0
        cnt = Counter(s)
        for k, v in cnt.items():
            ans = (ans + v * dp[(ord(k) - 97) + t]) % 1_000_000_007
        return ans
