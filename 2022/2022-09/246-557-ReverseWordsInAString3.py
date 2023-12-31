"""
Leetcode
557. Reverse Words in a String III (easy)
2022-09-22

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
"""


# Runtime: 75 ms, faster than 42.55% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.7 MB, less than 14.14% of Python3 online submissions for Reverse Words in a String III.
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(w[::-1] for w in s.split(' '))


s = Solution()
tests = [
    "Let's take LeetCode contest",
    "God Ding",
]
for t in tests:
    print(t)
    print(s.reverseWords(t))
    print()
