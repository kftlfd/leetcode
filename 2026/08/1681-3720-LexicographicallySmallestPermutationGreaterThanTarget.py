"""
Leetcode
2026-08-27
3720. Lexicographically Smallest Permutation Greater Than Target
Medium

You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 

Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

    The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
    The lexicographically smallest permutation that is strictly greater than target is "bca".

Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

    The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
    The lexicographically smallest permutation that is strictly greater than target is "eelt".

Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

    The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
    None of them is lexicographically strictly greater than target. Therefore, the answer is "".

 

Constraints:

    1 <= s.length == target.length <= 300
    s and target consist of only lowercase English letters.


Hint 1
Maintain frequency counts of s.
Hint 2
Walk left-to-right; if equal to target[i] is possible, take it and continue.
Hint 3
If not, try the smallest letter strictly greater than target[i].
Hint 4
If neither, backtrack left to the most recent index where you matched target and try to bump there.
"""


class Solution1:
    """
    leetcode solution 1: Sequential Enumeration
    Runtime 35ms Beats 15.79%
    Memory 19.27MB Beats 90.79%
    """

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        n = len(target)
        res = []

        for i in range(n):
            t = ord(target[i]) - ord("a")

            # Try placing the same character as target[i]
            if cnt[t] > 0:
                cnt[t] -= 1
                # 检查能否成功
                if self.can_greater(cnt, target[i + 1:]):
                    res.append(target[i])
                    continue
                cnt[t] += 1

            # Find a larger character
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1
                    res.append(chr(c + ord("a")))
                    # Lexicographically smallest permutation of remaining characters
                    res.append(
                        "".join(chr(j + ord("a")) * cnt[j] for j in range(26))
                    )
                    return "".join(res)

            # No feasible solution found
            return ""

        return ""

    def can_greater(self, cnt: list[int], suffix: str) -> bool:
        # Construct the largest string from largest to smallest
        max_str = "".join(
            chr(i + ord("a")) * cnt[i] for i in range(25, -1, -1) if cnt[i] > 0
        )
        return max_str > suffix


class Solution2:
    """
    leetcode solution 2: Reverse Greedy
    Runtime 3ms Beats 97.37%
    Memory 19.60MB Beats 18.42%
    """

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord("a")] += 1
            cnt[ord(target[i]) - ord("a")] -= 1

        # Try from right to left
        t = list(target)
        for i in range(len(s) - 1, -1, -1):
            b = ord(t[i]) - ord("a")
            cnt[b] += 1  # Reversal of consumption
            # Check if the prefix can fully match
            if min(cnt) < 0:
                continue
            # Find the smallest available character larger than b.
            for j in range(b + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    t[i] = chr(ord("a") + j)
                    return "".join(t[: i + 1]) + self.getMinString(cnt)

        return ""

    # Get the lexicographically smallest string (in ascending order)
    def getMinString(self, cnt: list[int]) -> str:
        res = []
        for i in range(26):
            res.append(chr(ord("a") + i) * cnt[i])
        return "".join(res)
