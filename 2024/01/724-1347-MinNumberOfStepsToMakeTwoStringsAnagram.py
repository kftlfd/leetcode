"""
Leetcode
1347. Minimum Number of Steps to Make Two Strings Anagram
Medium
2024-01-13

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 

 

Constraints:

    1 <= s.length <= 5 * 10^4
    s.length == t.length
    s and t consist of lowercase English letters only.
"""


from collections import Counter


class Solution:
    """
    Runtime: 184 ms, faster than 45.93% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
    Memory Usage: 18 MB, less than 11.97% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
    """

    def minSteps(self, s: str, t: str) -> int:
        count_c = Counter(s)
        ans = 0

        for c in t:
            if count_c[c] > 0:
                count_c[c] -= 1
            else:
                ans += 1

        return ans


class Solution1:
    """
    https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/solution/2208231
    Runtime: 93 ms, faster than 97.87% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
    Memory Usage: 18.1 MB, less than 5.24% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
    """

    def minSteps(self, s: str, t: str) -> int:
        return (Counter(s) - Counter(t)).total()
