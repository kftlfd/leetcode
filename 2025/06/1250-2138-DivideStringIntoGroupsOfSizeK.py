"""
Leetcode
2025-06-22
2138. Divide a String Into Groups of Size k
Easy

A string s can be partitioned into groups of size k using the following procedure:

    The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each element can be a part of exactly one group.
    For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.

Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.

Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.

 

Example 1:

Input: s = "abcdefghi", k = 3, fill = "x"
Output: ["abc","def","ghi"]
Explanation:
The first 3 characters "abc" form the first group.
The next 3 characters "def" form the second group.
The last 3 characters "ghi" form the third group.
Since all groups can be completely filled by characters from the string, we do not need to use fill.
Thus, the groups formed are "abc", "def", and "ghi".

Example 2:

Input: s = "abcdefghij", k = 3, fill = "x"
Output: ["abc","def","ghi","jxx"]
Explanation:
Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".

 

Constraints:

    1 <= s.length <= 100
    s consists of lowercase English letters only.
    1 <= k <= 100
    fill is a lowercase English letter.


Hint 1
Using the length of the string and k, can you count the number of groups the string can be divided into?
Hint 2
Try completing each group using characters from the string. If there aren’t enough characters for the last group, use the fill character to complete the group.
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.86MB Beats 36.31%
    """

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []

        for i in range(0, len(s), k):
            ans.append(s[i:i+k])

        if len(ans[-1]) != k:
            last = ans.pop()
            last = last + fill * (k - len(last))
            ans.append(last)

        return ans


class Solution1:
    """
    leetcode solution
    Runtime 0ms Beats 100.00%
    Memory 17.90MB Beats 36.31%
    """

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []  # grouped string
        n = len(s)
        curr = 0  # starting index of each group
        # split string
        while curr < n:
            res.append(s[curr: curr + k])
            curr += k
        # try to fill in the last group
        res[-1] += fill * (k - len(res[-1]))
        return res


class Solution2:
    """
    https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/editorial/comments/3044234/
    Runtime 0ms Beats 100.00%
    Memory 17.88MB Beats 36.31%
    """

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = [s[i: i + k] for i in range(0, len(s), k)]
        ans[-1] += fill * (k - len(ans[-1]))
        return ans
