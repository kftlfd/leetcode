"""
Leetcode
2024-11-01
1957. Delete Characters to Make Fancy String
Easy

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".

 

Constraints:

    1 <= s.length <= 10^5
    s consists only of lowercase English letters.
"""


class Solution:
    """
    Runtime: 164 ms, faster than 98.20% of Python3 online submissions for Delete Characters to Make Fancy String.
    Memory Usage: 18.7 MB, less than 21.72% of Python3 online submissions for Delete Characters to Make Fancy String.
    """

    def makeFancyString(self, s: str) -> str:
        cur_char = None
        count = 0
        ans = []

        for c in s:
            if c != cur_char:
                cur_char = c
                count = 0
            count += 1
            if count < 3:
                ans.append(c)

        return "".join(ans)
