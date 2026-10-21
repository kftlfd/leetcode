"""
Leetcode
2026-10-21
3863. Minimum Operations to Sort a String
Medium

You are given a string s consisting of lowercase English letters.

In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

 

Example 1:

Input: s = "dog"

Output: 1

Explanation:

    Sort substring "og" to "go".
    Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.

Example 2:

Input: s = "card"

Output: 2

Explanation:

    Sort substring "car" to "acr", so s = "acrd".
    Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.

Example 3:

Input: s = "gf"

Output: -1

Explanation:

    It is impossible to sort s under the given constraints. Thus, the answer is -1.

 

Constraints:

    1 <= s.length <= 10^5
    s consists of only lowercase English letters.


Hint 1
If s is already sorted, answer is 0.
Hint 2
Let mn be the minimum char and mx be the maximum char; if mn appears at the beginning (not whole string) or mx appears at the end (not whole string), answer is 1.
Hint 3
If s cannot be transformed into a sorted string, return -1.
"""


class Solution:
    """
    Wrong Answer
    1267 / 1291 testcases passed
    """

    def minOperations(self, s: str) -> int:
        if list(s) == sorted(s):
            return 0

        if len(s) == 2:
            return -1

        minc, maxc = min(s), max(s)

        if s[0] == minc or s[-1] == maxc:
            return 1

        return 2


class Solution1:
    """
    leetcode solution: Case Analysis
    Runtime 92ms Beats 68.94%
    Memory 19.70MB Beats 97.73%
    """

    def minOperations(self, s: str) -> int:
        n = len(s)
        mx, mn = max(s), min(s)
        if all(a <= b for a, b in zip(s, s[1:])):
            return 0
        if n == 2:
            return -1
        if s[0] == mn or s[-1] == mx:
            return 1
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2
        return 3
