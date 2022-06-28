"""
Leetcode
1647. Minimum Deletions to Make Character Frequencies Unique (medium)
2022-06-28


A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
"""

from collections import Counter


# Runtime: 234 ms, faster than 56.98% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
# Memory Usage: 14.8 MB, less than 51.90% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = [x for x in Counter(s).values()]
        ans = 0
        for i in range(len(cnt)):
            while cnt[i] > 0 and cnt[i] in cnt[:i] + cnt[i+1:]:
                cnt[i] -= 1
                ans += 1
        return ans


s = Solution()
tests = [
    "bbcebab",
    "aab",
    "aaabbbcc",
    "ceabaacb",
]
for t in tests:
    print(t)
    print(s.minDeletions(t))
    print()
