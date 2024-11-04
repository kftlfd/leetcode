"""
Leetcode
2024-11-04
3163. String Compression III
Medium

Given a string word, compress it using the following algorithm:

    Begin with an empty string comp. While word is not empty, use the following operation:
        Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
        Append the length of the prefix followed by c to comp.

Return the string comp.

 

Example 1:

Input: word = "abcde"

Output: "1a1b1c1d1e"

Explanation:

Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.

For each prefix, append "1" followed by the character to comp.

Example 2:

Input: word = "aaaaaaaaaaaaaabb"

Output: "9a5a2b"

Explanation:

Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.

    For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
    For prefix "aaaaa", append "5" followed by "a" to comp.
    For prefix "bb", append "2" followed by "b" to comp.

 

Constraints:

    1 <= word.length <= 2 * 10^5
    word consists only of lowercase English letters.
"""


class Solution:
    """
    Runtime: 128 ms, faster than 91.49% of Python3 online submissions for String Compression III.
    Memory Usage: 27.3 MB, less than 17.62% of Python3 online submissions for String Compression III.
    """

    def compressedString(self, word: str) -> str:
        cur_char = word[0]
        cur_count = 0
        ans = []

        for c in word:
            if cur_char != c:
                if cur_count > 0:
                    ans.append(f"{cur_count}{cur_char}")
                cur_char = c
                cur_count = 0
            cur_count += 1
            if cur_count >= 9:
                ans.append(f"{cur_count}{cur_char}")
                cur_count = 0

        if cur_count > 0:
            ans.append(f"{cur_count}{cur_char}")

        return "".join(ans)


class Solution1:
    """
    leetcode solution
    Runtime: 232 ms, faster than 59.58% of Python3 online submissions for String Compression III.
    Memory Usage: 28.4 MB, less than 8.56% of Python3 online submissions for String Compression III.
    """

    def compressedString(self, word: str) -> str:
        comp = []

        # pos tracks our position in the input string
        pos = 0

        # Process until we reach end of string
        while pos < len(word):
            consecutive_count = 0

            current_char = word[pos]

            # Count consecutive occurrences (maximum 9)
            while (
                pos < len(word)
                and consecutive_count < 9
                and word[pos] == current_char
            ):
                consecutive_count += 1
                pos += 1

            # Append count followed by character to the list
            comp.append(str(consecutive_count))
            comp.append(current_char)

        # Join the list into a single string for the final result
        return "".join(comp)
