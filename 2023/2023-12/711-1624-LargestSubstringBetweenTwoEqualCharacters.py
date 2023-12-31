"""
Leetcode
1624. Largest Substring Between Two Equal Characters
Easy
2023-12-31

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

 

Constraints:

    1 <= s.length <= 300
    s contains only lowercase English letters.
"""


class Solution:
    """
    Runtime: 71 ms, faster than 10.24% of Python3 online submissions for Largest Substring Between Two Equal Characters.
    Memory Usage: 17.1 MB, less than 13.41% of Python3 online submissions for Largest Substring Between Two Equal Characters.
    """

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = [None] * 26
        last = [None] * 26

        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            if first[index] is None:
                first[index] = i
            last[index] = i

        ans = -1

        for start, end in zip(first, last):
            if start != end:
                ans = max(ans, end - start - 1)

        return ans


sol = Solution()
tests = [
    ('aa',
     0),

    ('abca',
     2),

    ('cbzxy',
     -1),
]
for inp, exp in tests:
    res = sol.maxLengthBetweenEqualCharacters(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
