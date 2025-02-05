"""
Leetcode
2025-02-05
1790. Check if One String Swap Can Make Strings Equal
Easy
Topics
Companies
Hint

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

 

Constraints:

    1 <= s1.length, s2.length <= 100
    s1.length == s2.length
    s1 and s2 consist of only lowercase English letters.

Hint 1
The answer is false if the number of nonequal positions in the strings is not equal to 0 or 2.
Hint 2
Check that these positions have the same set of characters.
"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 18.00MB Beats 11.20%
    """

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap_chars = None
        swap = False

        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            if swap:
                return False
            if swap_chars is None:
                swap_chars = (c2, c1)
            elif (c1, c2) == swap_chars:
                swap = True
            else:
                return False

        return (swap and swap_chars is not None) or (not swap and swap_chars is None)


class Solution2:
    """
    leetcode solution 2: Only Check Differences
    Runtime 0ms Beats 100.00%
    Memory 17.65MB Beats 67.41%
    """

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_index_diff = 0
        second_index_diff = 0
        num_diffs = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diffs += 1
                # num_diffs is more than 2, one string swap will not make two strings equal
                if num_diffs > 2:
                    return False
                elif num_diffs == 1:
                    # store the index of first difference
                    first_index_diff = i
                else:
                    # store the index of second difference
                    second_index_diff = i
        # check if swap is possible
        return (
            s1[first_index_diff] == s2[second_index_diff]
            and s1[second_index_diff] == s2[first_index_diff]
        )
