"""
Leetcode
1239. Maximum Length of a Concatenated String with Unique Characters (medium)
2022-10-24

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
"""

from typing import List, Optional


# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/2737493/PythonC++JavaRust-0-ms-bit-and-set-operations-(with-detailed-comments)
#     Runtime: 210 ms, faster than 56.06% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
# Memory Usage: 52 MB, less than 11.15% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        # filter for strings with no cuplicate characters
        unique = []
        for s in arr:
            u = set(s)
            if len(s) == len(u):
                unique.append(u)

        # try adding strings together
        concat = [set()]
        for u in unique:
            for c in concat:
                if not c & u:
                    concat.append(c | u)

        return max(len(s) for s in concat)


# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/2737783/Python's-Simple-and-Easy-to-Understand-Solution-or-99-Faster
# Runtime: 260 ms, faster than 39.71% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
# Memory Usage: 18.5 MB, less than 24.57% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
class Solution1:
    def maxLength(self, arr: List[str]) -> int:
        res = [""]
        ans = 0

        for word in arr:
            for r in res:
                newRes = word + r
                if len(newRes) == len(set(newRes)):
                    res.append(newRes)
                    ans = max(ans, len(newRes))

        return ans


s = Solution1()
tests = [
    (["un", "iq", "ue"],
     4),

    (["cha", "r", "act", "ers"],
     6),

    (["abcdefghijklmnopqrstuvwxyz"],
     26),

]
for inp, exp in tests:
    res = s.maxLength(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
