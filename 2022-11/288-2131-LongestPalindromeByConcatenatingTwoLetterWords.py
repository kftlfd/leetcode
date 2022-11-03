"""
Leetcode
2131. Longest Palindrome by Concatenating Two Letter Words (medium)
2022-11-03

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
"""

from typing import List, Optional
from collections import defaultdict, Counter


# Runtime: 2952 ms, faster than 54.78% of Python3 online submissions for Longest Palindrome by Concatenating Two Letter Words.
# Memory Usage: 38.3 MB, less than 54.38% of Python3 online submissions for Longest Palindrome by Concatenating Two Letter Words.
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        ans = 0
        counter = Counter(words)
        seen = set()
        center = False

        for word in counter:

            pair = word[::-1]

            if word == pair:
                count = counter[word]
                if count % 2 == 0:
                    ans += count
                    continue
                ans += count - 1
                if not center:
                    ans += 1
                    center = True
                continue

            if pair in seen or pair not in counter:
                continue

            seen.add(word)
            count = min(counter[word], counter[pair])
            ans += count * 2

        return ans * 2


s = Solution()
tests = [
    (["lc", "cl", "gg"],
     6),

    (["ab", "ty", "yt", "lc", "cl", "ab"],
        8),

    (["cc", "ll", "xx"],
     2),
]
for inp, exp in tests:
    res = s.longestPalindrome(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
