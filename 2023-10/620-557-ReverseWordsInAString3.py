"""
Leetcode
557. Reverse Words in a String III (easy)
2023-10-01

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"

 

Constraints:

    1 <= s.length <= 5 * 10^4
    s contains printable ASCII characters.
    s does not contain any leading or trailing spaces.
    There is at least one word in s.
    All the words in s are separated by a single space.
"""


class Solution:
    """
    Runtime: 42 ms, faster than 68.53% of Python3 online submissions for Reverse Words in a String III.
    Memory Usage: 16.9 MB, less than 67.63% of Python3 online submissions for Reverse Words in a String III.
    """

    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))


class Solution1:
    """
    Runtime: 81 ms, faster than 12.58% of Python3 online submissions for Reverse Words in a String III.
    Memory Usage: 17.2 MB, less than 16.58% of Python3 online submissions for Reverse Words in a String III.
    """

    def reverseWords(self, s: str) -> str:
        ans = []
        word = []

        for c in s:
            if c == " ":
                while word:
                    ans.append(word.pop())
                ans.append(c)
            else:
                word.append(c)

        while word:
            ans.append(word.pop())

        return "".join(ans)
