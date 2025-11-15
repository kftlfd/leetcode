"""
Leetcode
2025-11-15
3234. Count the Number of Substrings With Dominant Ones
Medium

You are given a binary string s.

Return the number of

with dominant ones.

A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

 

Example 1:

Input: s = "00011"

Output: 5

Explanation:

The substrings with dominant ones are shown in the table below.
i	j	s[i..j]	Number of Zeros	Number of Ones
3	3	1	0	1
4	4	1	0	1
2	3	01	1	1
3	4	11	0	2
2	4	011	1	2

Example 2:

Input: s = "101101"

Output: 16

Explanation:

The substrings with non-dominant ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.
i	j	s[i..j]	Number of Zeros	Number of Ones
1	1	0	1	0
4	4	0	1	0
1	4	0110	2	2
0	4	10110	2	3
1	5	01101	2	3

 

Constraints:

    1 <= s.length <= 4 * 10^4
    s consists only of characters '0' and '1'.

Hint 1
Let us fix the starting index l of the substring and count the number of indices r such that l <= r and the substring s[l..r] has dominant ones.
Hint 2
A substring with dominant ones has at most sqrt(n) zeros.
Hint 3
We cannot iterate over every r and check if the s[l..r] has dominant ones. Instead, we iterate over the next sqrt(n) zeros to the left of l and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.
"""


class Solution1:
    """
    leetcode solution: Enumeration
    Runtime 6498ms Beats 84.48%
    Memory 19.21MB Beats 51.72%
    """

    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res
