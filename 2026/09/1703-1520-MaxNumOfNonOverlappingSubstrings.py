"""
Leetcode
2026-09-18
1520. Maximum Number of Non-Overlapping Substrings
Hard

Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

    The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
    A substring that contains a certain character c must also contain all occurrences of c.

Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

 

Constraints:

    1 <= s.length <= 10^5
    s contains only lowercase English letters.


Hint 1
Notice that it's impossible for any two valid substrings to overlap unless one is inside another.
Hint 2
We can start by finding the starting and ending index for each character.
Hint 3
From these indices, we can form the substrings by expanding each character's range if necessary (if another character exists in the range with smaller/larger starting/ending index).
Hint 4
Sort the valid substrings by length and greedily take those with the smallest length, discarding the ones that overlap those we took.
"""

from typing import List, Optional


class Solution:
    """
    Wrong Answer
    """

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        occ_first, occ_last = {}, {}

        for i, c in enumerate(s):
            if c not in occ_first:
                occ_first[c] = i
            occ_last[c] = i

        substrs = sorted((
            (s[occ_first[c]:occ_last[c]+1], occ_first[c], occ_last[c])
            for c in occ_first.keys()
        ), key=lambda x: len(x[0]))

        ans = []

        for substr, l, r in substrs:
            ok = True
            for _, xl, xr in ans:
                if (xl >= l and xr <= r) or (l >= xl and r <= xr):
                    ok = False
                    break
            if ok:
                ans.append((substr, l, r))

        return [x[0] for x in ans]


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 1429ms Beats 12.39%
    Memory 20.16MB Beats 98.23%
    """

    class Seg:
        def __init__(self, left=-1, right=-1):
            self.left = left
            self.right = right

        def __lt__(self, rhs):
            return (
                self.left > rhs.left
                if self.right == rhs.right
                else self.right < rhs.right
            )

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        seg = [self.Seg() for _ in range(26)]
        # Preprocess the left and right endpoints.
        for i in range(len(s)):
            char_idx = ord(s[i]) - ord("a")
            if seg[char_idx].left == -1:
                seg[char_idx].left = seg[char_idx].right = i
            else:
                seg[char_idx].right = i

        for i in range(26):
            if seg[i].left != -1:
                j = seg[i].left
                while j <= seg[i].right:
                    char_idx = ord(s[j]) - ord("a")
                    if (
                        seg[i].left <= seg[char_idx].left
                        and seg[char_idx].right <= seg[i].right
                    ):
                        pass
                    else:
                        seg[i].left = min(seg[i].left, seg[char_idx].left)
                        seg[i].right = max(seg[i].right, seg[char_idx].right)
                        j = seg[i].left
                    j += 1

        # Greedily select intervals.
        seg.sort()
        ans = []
        end = -1
        for segment in seg:
            left, right = segment.left, segment.right
            if left == -1:
                continue
            if end == -1 or left > end:
                end = right
                ans.append(s[left: right + 1])

        return ans


class Solution2:
    """
    sample 175ms solution
    Runtime 191ms Beats 69.03%
    Memory 20.52MB Beats 38.94%
    """

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find the first and last occurrence for each character
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i

        # Step 2: Expand intervals to satisfy condition 2 (if a substring contains c, it must contain all occurrences of c)
        intervals = []
        for char in first:
            left, right = first[char], last[char]
            valid = True
            i = left
            while i <= right:
                # If any character appears before our current left bound, we must expand our left bound
                if first[s[i]] < left:
                    valid = False
                    break
                # Update the right bound if necessary
                right = max(right, last[s[i]])
                i += 1
            if valid:
                intervals.append([left, right])

        # Step 3: Sort intervals by their end points, and then by length (or vice versa)
        # We want to pick non-overlapping intervals greedily
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1
        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result
