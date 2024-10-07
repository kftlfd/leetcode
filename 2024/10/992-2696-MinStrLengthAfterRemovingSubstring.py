"""
Leetcode
2024-10-07
2696. Minimum String Length After Removing Substrings
Easy

You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

 

Example 1:

Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.

Example 2:

Input: s = "ACBBD"
Output: 5
Explanation: We cannot do any operations on the string so the length remains the same.

 

Constraints:

    1 <= s.length <= 100
    s consists only of uppercase English letters.
"""


class Solution:
    """
    Runtime: 41 ms, faster than 73.16% of Python3 online submissions for Minimum String Length After Removing Substrings.
    Memory Usage: 16.6 MB, less than 7.81% of Python3 online submissions for Minimum String Length After Removing Substrings.
    """

    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            if stack and ((c == "B" and stack[-1] == "A") or (c == "D" and stack[-1] == "C")):
                stack.pop()
            else:
                stack.append(c)

        return len(stack)


class Solution3:
    """
    leetcode solution 3: In Place Modification
    Runtime: 46 ms, faster than 46.10% of Python3 online submissions for Minimum String Length After Removing Substrings.
    Memory Usage: 16.5 MB, less than 41.77% of Python3 online submissions for Minimum String Length After Removing Substrings.
    """

    def minLength(self, s: str) -> int:
        char_list = list(s)
        write_ptr = 0

        # Iterate over each character in the string
        for read_ptr in range(len(s)):
            # Write the current character to the current write position
            char_list[write_ptr] = char_list[read_ptr]

            # Check if we have a valid pattern to remove
            if (
                write_ptr > 0
                and char_list[write_ptr - 1] in "AC"
                and ord(char_list[write_ptr])
                == ord(char_list[write_ptr - 1]) + 1
            ):
                write_ptr -= 1
            else:
                write_ptr += 1  # No match, so move the write pointer forward

        # The write_ptr now represents the length of the remaining string
        return write_ptr
