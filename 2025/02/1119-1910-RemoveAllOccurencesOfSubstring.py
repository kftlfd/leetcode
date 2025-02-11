"""
Leetcode
2025-02-11
1910. Remove All Occurrences of a Substring
Medium
Topics
Companies
Hint

Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

    Find the leftmost occurrence of the substring part and remove it from s.

Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".

Example 2:

Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".

 

Constraints:

    1 <= s.length <= 1000
    1 <= part.length <= 1000
    s and part consists of lowercase English letters.


Hint 1
Note that a new occurrence of pattern can appear if you remove an old one, For example, s = "ababcc" and pattern = "abc".
Hint 2
You can maintain a stack of characters and if the last character of the pattern size in the stack match the pattern remove them
"""


class Solution:
    """
    Runtime 9ms Beats 31.57%
    Memory 17.88MB Beats 51.53%
    """

    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = list(part)
        n = len(part)

        for c in s:
            stack.append(c)
            if stack[-n:] == part:
                stack[-n:] = []

        return "".join(stack)


class Solution1:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.73MB Beats 75.36%
    """

    def removeOccurrences(self, s: str, part: str) -> str:
        ans = s
        while part in ans:
            ans = ans.replace(part, "", 1)
        return ans


class Solution3:
    """
    leetcode solution 3: Knuth-Morris-Pratt (KMP) Algorithm
    Runtime 9ms Beats 31.57%
    Memory 17.92MB Beats 32.79%
    """

    def removeOccurrences(self, s: str, part: str) -> str:
        # Precompute KMP longest prefix-suffix array for the pattern
        kmp_lps = self._compute_longest_prefix_suffix(part)

        # Using list as a stack to track characters and support pattern matching
        char_stack = []

        # Array to store pattern matching indices during traversal
        pattern_indexes = [0] * (len(s) + 1)

        str_index = 0
        pattern_index = 0
        while str_index < len(s):
            current_char = s[str_index]
            char_stack.append(current_char)

            if current_char == part[pattern_index]:
                # Track the next pattern index when characters match
                pattern_indexes[len(char_stack)] = pattern_index + 1
                pattern_index += 1

                if pattern_index == len(part):
                    # Remove entire matched pattern from stack
                    for _ in range(len(part)):
                        char_stack.pop()

                    # Restore pattern index for next potential match
                    pattern_index = (
                        0
                        if not char_stack
                        else pattern_indexes[len(char_stack)]
                    )
            else:
                if pattern_index != 0:
                    # Backtrack pattern matching using KMP LPS
                    str_index -= 1
                    pattern_index = kmp_lps[pattern_index - 1]
                    char_stack.pop()
                else:
                    # Reset pattern index tracking when no match is possible
                    pattern_indexes[len(char_stack)] = 0

            str_index += 1

        # Convert remaining stack characters to result string
        return "".join(char_stack)

    def _compute_longest_prefix_suffix(self, pattern: str) -> list:
        # Array to store the longest proper prefix which is also a suffix
        lps = [0] * len(pattern)

        # Initialize tracking variables for prefix and current position
        current = 1
        prefix_length = 0
        while current < len(pattern):
            # If characters match, extend the prefix length
            if pattern[current] == pattern[prefix_length]:
                # Store the length of matching prefix
                prefix_length += 1
                lps[current] = prefix_length
                current += 1

            # If characters don't match and we're not at the start of the pattern
            elif prefix_length != 0:
                # Backtrack to the previous longest prefix-suffix
                prefix_length = lps[prefix_length - 1]

            # If no match and no prefix to backtrack
            else:
                # No prefix-suffix match found
                lps[current] = 0
                current += 1

        # Return the computed longest prefix-suffix array
        return lps
