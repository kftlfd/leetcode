"""
Leetcode
2026-07-21
3499. Maximize Active Section with Trade I
Medium

You are given a binary string s of length n, where:

    '1' represents an active section.
    '0' represents an inactive section.

You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

    Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
    Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.

Return the maximum number of active sections in s after making the optimal trade.

Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.

 

Example 1:

Input: s = "01"

Output: 1

Explanation:

Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 2:

Input: s = "0100"

Output: 4

Explanation:

    String "0100" → Augmented to "101001".
    Choose "0100", convert "101001" → "100001" → "111111".
    The final string without augmentation is "1111". The maximum number of active sections is 4.

Example 3:

Input: s = "1000100"

Output: 7

Explanation:

    String "1000100" → Augmented to "110001001".
    Choose "000100", convert "110001001" → "110000001" → "111111111".
    The final string without augmentation is "1111111". The maximum number of active sections is 7.

Example 4:

Input: s = "01010"

Output: 4

Explanation:

    String "01010" → Augmented to "1010101".
    Choose "010", convert "1010101" → "1000101" → "1111101".
    The final string without augmentation is "11110". The maximum number of active sections is 4.

 

Constraints:

    1 <= n == s.length <= 10^5
    s[i] is either '0' or '1'


Hint 1
Split the string into several zero-one segments.
Hint 2
For each one-segment, if it has two neighbors (i.e., it is surrounded by two zero-segments), the total sum of their lengths is one of the candidates for delta.
Hint 3
Find the maximum delta and add it to the total number of ones in the string.
"""


class Solution:
    """
    Runtime 849ms Beats 40.19%
    Memory 27.71MB Beats 8.41%
    """

    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = 0
        segments = []
        cur_val = 1
        cur_cnt = 0

        for c in s:
            val = 0
            if c == "1":
                val = 1
                ones += 1

            if val == cur_val:
                cur_cnt += 1
            else:
                segments.append((cur_val, cur_cnt))
                cur_val ^= 1
                cur_cnt = 1

        segments.append((cur_val, cur_cnt))

        if cur_val == 0:
            segments.append((1, 1))

        delta = 0

        for i in range(1, len(segments) - 1):
            if segments[i][0] == 1:
                left, right = segments[i-1], segments[i+1]
                if left[0] == 0 and right[0] == 0:
                    delta = max(delta, left[1] + right[1])

        return ones + delta


class Solution1:
    """
    leetcode solution 1: Greedy
    Runtime 629ms Beats 66.35%
    Memory 21.08MB Beats 61.68%
    """

    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        cnt1 = s.count("1")

        zeroBlocks = []
        i = 0
        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1

            if s[start] == "0":
                zeroBlocks.append(i - start)

        m = len(zeroBlocks)

        if m < 2:
            return cnt1

        bestGain = 0  # Optimal Increment
        for i in range(m - 1):
            bestGain = max(bestGain, zeroBlocks[i] + zeroBlocks[i + 1])
        return cnt1 + bestGain


class Solution2:
    """
    leetcode solution 2: Space Optimization
    Runtime 573ms Beats 85.05%
    Memory 20.92MB Beats 65.42%
    """

    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        cnt1 = s.count("1")

        n = len(s)
        i = 0

        bestGain = 0
        prev = float("-inf")

        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1

            if s[start] == "0":
                cur = i - start
                bestGain = max(bestGain, prev + cur)
                prev = cur

        return int(cnt1 + bestGain)
