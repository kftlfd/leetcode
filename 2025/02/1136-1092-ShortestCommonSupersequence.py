"""
Leetcode
2025-02-28
1092. Shortest Common Supersequence
Hard

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"

 

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of lowercase English letters.


Hint 1
We can find the length of the longest common subsequence between str1[i:] and str2[j:] (for all (i, j)) by using dynamic programming.
Hint 2
We can use this information to recover the shortest common supersequence.
"""


class Solution1:
    """
    leetcode solution 1: Backtracking (Time Limit Exceeded)
    """

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Base case: both strings are empty
        if not str1 and not str2:
            return ""

        # Base case: one string is empty, append the other string
        if not str1:
            return str2
        if not str2:
            return str1

        # If the first characters match, include it in the supersequence
        if str1[0] == str2[0]:
            return str1[0] + self.shortestCommonSupersequence(
                str1[1:], str2[1:]
            )
        else:
            # Try both options: picking from str1 or str2, and choose the shorter one
            pick_str1 = str1[0] + self.shortestCommonSupersequence(
                str1[1:], str2
            )
            pick_str2 = str2[0] + self.shortestCommonSupersequence(
                str1, str2[1:]
            )

            return pick_str1 if len(pick_str1) < len(pick_str2) else pick_str2


class Solution2:
    """
    leetcode solution 2: Memoization (Memory Limit Exceeded)
    """

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = {}
        return self.helper(str1, str2, memo)

    def helper(self, str1: str, str2: str, memo: dict) -> str:
        memo_key = (str1, str2)
        # Check if result is already computed
        if memo_key in memo:
            return memo[memo_key]

        # Base case: both strings are empty
        if not str1 and not str2:
            return ""

        # Base case: one string is empty, append the other string
        if not str1:
            return str2
        if not str2:
            return str1

        # If the first characters match, include it in the supersequence
        if str1[0] == str2[0]:
            memo[memo_key] = str1[0] + self.helper(str1[1:], str2[1:], memo)
            return memo[memo_key]

        # Try both options: picking from str1 or str2, and choose the shorter one
        pick_str1 = str1[0] + self.helper(str1[1:], str2, memo)
        pick_str2 = str2[0] + self.helper(str1, str2[1:], memo)

        memo[memo_key] = (
            pick_str1 if len(pick_str1) < len(pick_str2) else pick_str2
        )
        return memo[memo_key]


class Solution3:
    """
    leetcode solution 3: Bottom-Up Dynamic Programming
    """

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)

        # Initialize the first row (when str1 is empty, the supersequence is str2's prefix)
        prev_row = [str2[0:col] for col in range(str2_length + 1)]

        # Fill the DP table row by row
        for row in range(1, str1_length + 1):
            # Initialize the first column (when str2 is empty, the supersequence is str1's prefix)
            curr_row = [str1[0:row]] + [None for _ in range(str2_length)]

            for col in range(1, str2_length + 1):
                # If characters match, extend the supersequence from the diagonal value
                if str1[row - 1] == str2[col - 1]:
                    curr_row[col] = prev_row[col - 1] + str1[row - 1]
                else:
                    # If characters do not match, choose the shorter supersequence
                    # From previous row (exclude current str1 char)
                    pick_s1 = prev_row[col]
                    # From previous column (exclude current str2 char)
                    pick_s2 = curr_row[col - 1]

                    curr_row[col] = (
                        pick_s1 + str1[row - 1]
                        if len(pick_s1) < len(pick_s2)
                        else pick_s2 + str2[col - 1]
                    )

            # Move to the next row (update previous row reference)
            prev_row = curr_row

        # Return the shortest common supersequence from the last cell
        return prev_row[str2_length]


class Solution4:
    """
    leetcode solution 4: Most Optimal - Space Optimized Dynamic Programming
    Runtime 467ms Beats 40.84%
    Memory 56.33MB Beats 26.37%
    """

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)

        dp = [
            [0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)
        ]

        # Initialize the base cases
        # When str2 is empty, the supersequence is str1 itself (length = row index)
        for row in range(str1_length + 1):
            dp[row][0] = row

        # When str1 is empty, the supersequence is str2 itself (length = col index)
        for col in range(str2_length + 1):
            dp[0][col] = col

        # Fill the DP table
        for row in range(1, str1_length + 1):
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    # If characters match, inherit the length from the diagonal +1
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    # If characters do not match, take the minimum length option +1
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

        super_sequence = []
        row, col = str1_length, str2_length

        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                # If characters match, take it from diagonal
                super_sequence.append(str1[row - 1])
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                # If str1’s character is part of the supersequence, move up
                super_sequence.append(str1[row - 1])
                row -= 1
            else:
                # If str2’s character is part of the supersequence, move left
                super_sequence.append(str2[col - 1])
                col -= 1

        # Append any remaining characters
        # If there are leftover characters in str1
        while row > 0:
            super_sequence.append(str1[row - 1])
            row -= 1
        # If there are leftover characters in str2
        while col > 0:
            super_sequence.append(str2[col - 1])
            col -= 1

        # Reverse the built sequence to get the correct order
        return "".join(super_sequence[::-1])
