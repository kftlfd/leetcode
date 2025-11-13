"""
Leetcode
2025-11-13
3228. Maximum Number of Operations to Move Ones to the End
Medium

You are given a binary string s.

You can perform the following operation on the string any number of times:

    Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
    Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".

Return the maximum number of operations that you can perform.

 

Example 1:

Input: s = "1001101"

Output: 4

Explanation:

We can perform the following operations:

    Choose index i = 0. The resulting string is s = "0011101".
    Choose index i = 4. The resulting string is s = "0011011".
    Choose index i = 3. The resulting string is s = "0010111".
    Choose index i = 2. The resulting string is s = "0001111".

Example 2:

Input: s = "00111"

Output: 0

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is either '0' or '1'.


Hint 1
It is optimal to perform the operation on the lowest index possible each time.
Hint 2
Traverse the string from left to right and perform the operation every time it is possible.
"""


class Solution:
    """
    Time Limit Exceeded
    672 / 694 testcases passed
    """

    def maxOperations(self, s: str) -> int:
        ans = 0
        nums = list(s)
        n = len(nums)
        start = 0

        changes = True
        while changes:
            changes = False
            while start < n and nums[start] == "0":
                start += 1
            for i in range(start, n - 1):
                if nums[i] != "1" or nums[i + 1] != "0":
                    continue
                swap_idx = i + 1
                while swap_idx + 1 < n and nums[swap_idx + 1] == "0":
                    swap_idx += 1
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
                changes = True
                ans += 1

        return ans


class Solution1:
    """
    leetcode solution: Greedy + Counting
    Runtime 91ms Beats 19.16%
    Memory 18.29MB Beats 40.72%
    """

    def maxOperations(self, s: str) -> int:
        count_one = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == "0":
                while i + 1 < len(s) and s[i + 1] == "0":
                    i += 1
                ans += count_one
            else:
                count_one += 1
            i += 1
        return ans
