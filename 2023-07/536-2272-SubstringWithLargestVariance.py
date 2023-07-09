"""
Leetcode
2272. Substring With Largest Variance (hard)
2023-07-09

The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.

Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.

Constraints:

    1 <= s.length <= 10^4
    s consists of lowercase English letters.
"""

from collections import defaultdict


class Solution:
    """
    leetcode solution
    Kadane's algorithm
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    https://leetcode.com/problems/substring-with-largest-variance/solution/1962299
    Runtime: 1094 ms, faster than 99.15% of Python3 online submissions for Substring With Largest Variance.
    Memory Usage: 17 MB, less than 5.98% of Python3 online submissions for Substring With Largest Variance.
    """

    def largestVariance(self, s: str) -> int:
        res = 0
        char_pos = defaultdict(list)

        for i, c in enumerate(s):
            char_pos[c].append(i)

        for a in char_pos.keys():
            for b in char_pos.keys():
                if a == b:
                    continue
                a_idx = b_idx = 0
                a_count = b_count = 0
                A = len(char_pos[a])
                B = len(char_pos[b])

                while a_idx < A or b_idx < B:
                    if a_idx < A and (b_idx == B or char_pos[a][a_idx] < char_pos[b][b_idx]):
                        a_count += 1
                        a_idx += 1
                    elif b_idx < B:
                        b_count += 1
                        b_idx += 1
                    if b_count < a_count and a_idx < A:
                        a_count = b_count = 0
                    if a_count > 0 < b_count:
                        res = max(res, b_count - a_count)

        return res


s = Solution()
tests = [
    ("aababbb",
     3),

    ("abcde",
     0),
]
for inp, exp in tests:
    res = s.largestVariance(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
