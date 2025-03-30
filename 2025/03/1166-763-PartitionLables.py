"""
Leetcode
2025-03-30
763. Partition Labels
Medium

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]

 

Constraints:

    1 <= s.length <= 500
    s consists of lowercase English letters.


Hint 1
Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.
"""

from typing import List


class Solution:
    """
    Runtime 4ms Beats 65.08%
    Memory 17.65MB Beats 85.21%
    """

    def partitionLabels(self, s: str) -> List[int]:
        chars = [[None, 0] for _ in range(26)]
        a = ord('a')

        for idx, c in enumerate(s):
            i = ord(c) - a
            if chars[i][0] is None:
                chars[i][0] = idx
            chars[i][1] = idx

        prev_start = 0
        prev_end = 0
        ans = []

        for start, end in sorted(x for x in chars if x[0] is not None):
            if start > prev_end:
                ans.append(start - prev_start)
                prev_start = start
            prev_end = max(prev_end, end)

        ans.append(prev_end + 1 - prev_start)

        return ans


class Solution1:
    """
    leetcode solution 1: Two Pointers
    Runtime 8ms Beats 17.27%
    Memory 17.58MB Beats 97.48%
    """

    def partitionLabels(self, s: str) -> List[int]:
        # Stores the last index of each character in 's'
        last_occurrence = [0] * 26
        for i, char in enumerate(s):
            last_occurrence[ord(char) - ord("a")] = i

        partition_end = 0
        partition_start = 0
        partition_sizes = []

        for i, char in enumerate(s):
            partition_end = max(
                partition_end, last_occurrence[ord(char) - ord("a")]
            )
            # End of the current partition
            if i == partition_end:
                partition_sizes.append(i - partition_start + 1)
                partition_start = i + 1

        return partition_sizes


class Solution2:
    """
    leetcode solution 2: Merge Intervals
    Runtime 7ms Beats 41.22%
    Memory 17.66MB Beats 85.21%
    """

    def partitionLabels(self, s: str) -> List[int]:
        partition_sizes = []
        last_occurrence = [0] * 26
        first_occurrence = [-1] * 26

        partition_start, partition_end = 0, 0

        # Store the last occurrence index of each character
        for i, char in enumerate(s):
            last_occurrence[ord(char) - ord("a")] = i

        for i, char in enumerate(s):
            index = ord(char) - ord("a")

            # Store the first occurrence index of each character (if not set)
            if first_occurrence[index] == -1:
                first_occurrence[index] = i

            # If we find a new partition start
            if partition_end < first_occurrence[index]:
                partition_sizes.append(partition_end - partition_start + 1)
                partition_start = i
                partition_end = i

            # Update partition end boundary
            partition_end = max(partition_end, last_occurrence[index])

        # Add the last partition if it exists
        if partition_end - partition_start + 1 > 0:
            partition_sizes.append(partition_end - partition_start + 1)

        return partition_sizes
