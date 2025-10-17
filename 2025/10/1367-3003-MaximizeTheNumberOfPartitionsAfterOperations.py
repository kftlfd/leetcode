"""
Leetcode
2025-10-17
3003. Maximize the Number of Partitions After Operations
Hard

You are given a string s and an integer k.

First, you are allowed to change at most one index in s to another lowercase English letter.

After that, do the following partitioning operation until s is empty:

    Choose the longest prefix of s containing at most k distinct characters.
    Delete the prefix from s and increase the number of partitions by one. The remaining characters (if any) in s maintain their initial order.

Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

 

Example 1:

Input: s = "accca", k = 2

Output: 3

Explanation:

The optimal way is to change s[2] to something other than a and c, for example, b. then it becomes "acbca".

Then we perform the operations:

    The longest prefix containing at most 2 distinct characters is "ac", we remove it and s becomes "bca".
    Now The longest prefix containing at most 2 distinct characters is "bc", so we remove it and s becomes "a".
    Finally, we remove "a" and s becomes empty, so the procedure ends.

Doing the operations, the string is divided into 3 partitions, so the answer is 3.

Example 2:

Input: s = "aabaab", k = 3

Output: 1

Explanation:

Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

Example 3:

Input: s = "xxyz", k = 1

Output: 4

Explanation:

The optimal way is to change s[0] or s[1] to something other than characters in s, for example, to change s[0] to w.

Then s becomes "wxyz", which consists of 4 distinct characters, so as k is 1, it will divide into 4 partitions.

 

Constraints:

    1 <= s.length <= 10^4
    s consists only of lowercase English letters.
    1 <= k <= 26


Hint 1
For each position, try to brute-force the replacements.
Hint 2
To speed up the brute-force solution, we can precompute the following (without changing any index) using prefix sums and binary search:
- pref[i]: The number of resulting partitions from the operations by performing the operations on s[0:i].
- suff[i]: The number of resulting partitions from the operations by performing the operations on s[i:n - 1], where n == s.length.
- partition_start[i]: The start index of the partition containing the ith index after performing the operations.
Hint 3
Now, for a position i, we can try all possible 25 replacements:
For a replacement, using prefix sums and binary search, we need to find the rightmost index, r, such that the number of distinct characters in the range [partition_start[i], r] is at most k.
There are 2 cases:
- r >= i: the number of resulting partitions in this case is 1 + pref[partition_start[i] - 1] + suff[r + 1].
- Otherwise, we need to find the rightmost index r2 such that the number of distinct characters in the range [r:r2] is at most k. The answer in this case is 2 + pref[partition_start[i] - 1] + suff[r2 + 1]
Hint 4
The answer is the maximum among all replacements.
"""


class Solution:
    """
    leetcode solution: Bitwise Operations + Preprocessing + Enumeration
    Runtime 47ms Beats 55.17%
    Memory 20.48MB Beats 53.45%
    """

    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        left = [[0] * 3 for _ in range(n)]
        right = [[0] * 3 for _ in range(n)]

        num, mask, count = 0, 0, 0
        for i in range(n - 1):
            binary = 1 << (ord(s[i]) - ord("a"))
            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            left[i + 1][0] = num
            left[i + 1][1] = mask
            left[i + 1][2] = count

        num, mask, count = 0, 0, 0
        for i in range(n - 1, 0, -1):
            binary = 1 << (ord(s[i]) - ord("a"))
            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            right[i - 1][0] = num
            right[i - 1][1] = mask
            right[i - 1][2] = count

        max_val = 0
        for i in range(n):
            seg = left[i][0] + right[i][0] + 2
            tot_mask = left[i][1] | right[i][1]
            tot_count = bin(tot_mask).count("1")
            if left[i][2] == k and right[i][2] == k and tot_count < 26:
                seg += 1
            elif min(tot_count + 1, 26) <= k:
                seg -= 1
            max_val = max(max_val, seg)
        return max_val
