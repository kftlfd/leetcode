"""
Leetcode
2025-01-13
3223. Minimum Length of String After Operations
Medium

You are given a string s.

You can perform the following process on s any number of times:

    Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
    Delete the closest character to the left of index i that is equal to s[i].
    Delete the closest character to the right of index i that is equal to s[i].

Return the minimum length of the final string s that you can achieve.

 

Example 1:

Input: s = "abaacbcbb"

Output: 5

Explanation:
We do the following operations:

    Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
    Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".

Example 2:

Input: s = "aa"

Output: 2

Explanation:
We cannot perform any operations, so we return the length of the original string.

 

Constraints:

    1 <= s.length <= 2 * 10^5
    s consists only of lowercase English letters.

Hint 1
Only the frequency of each character matters in finding the final answer.
Hint 2
If a character occurs less than 3 times, we cannot perform any process with it.
Hint 3
Suppose there is a character that occurs at least 3 times in the string, we can repeatedly delete two of these characters until there are at most 2 occurrences left of it.
"""

from collections import Counter


class Solution:
    """
    Runtime 136ms Beats 60.63%
    Memory 19.02MB Beats 5.71%
    """

    def minimumLength(self, s: str) -> int:
        return sum((n - 1) % 2 + 1 for n in Counter(s).values())


class Solution2:
    """
    leetcode solution 2: Using Frequency Array
    Runtime 239ms Beats 24.44%
    Memory 18.92MB Beats 14.92%
    """

    def minimumLength(self, s: str) -> int:
        # Step 1: Initialize a frequency array to count occurrences of each character
        char_frequency = [0] * 26
        total_length = 0

        # Step 2: Count the frequency of each character in the string
        for current_char in s:
            char_frequency[ord(current_char) - ord("a")] += 1

        # Step 3: Calculate the total length after deletions count
        for frequency in char_frequency:
            if frequency == 0:
                continue  # Skip characters that don't appear
            if frequency % 2 == 0:
                total_length += 2  # If frequency is even, add 2 characters
            else:
                total_length += 1  # If frequency is odd, add 1 character

        # Step 4: Return the minimum length after deletions count
        return total_length
