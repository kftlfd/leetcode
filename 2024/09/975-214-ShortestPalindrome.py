"""
Leetcode
2024-09-20
214. Shortest Palindrome
Hard

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: s = "abcd"
Output: "dcbabcd"

 

Constraints:

    0 <= s.length <= 5 * 10^4
    s consists of lowercase English letters only.
"""


class Solution:
    """
    Time Limit Exceeded (122 / 123 test cases passed.)
    """

    def shortestPalindrome(self, s: str) -> str:
        ans = ""

        for cur_end in range(len(s) - 1, -1, -1):
            is_pali = True
            start = 0
            end = cur_end
            while start <= end:
                if s[start] != s[end]:
                    is_pali = False
                    break
                start += 1
                end -= 1
            if is_pali:
                add = s[cur_end + 1:][::-1]
                ans = add + s
                break

        return ans


class Solution3:
    """
    leetcode solution 3: KMP (Knuth-Morris-Pratt) Algorithm
    Runtime: 39 ms, faster than 98.87% of Python3 online submissions for Shortest Palindrome.
    Memory Usage: 20.7 MB, less than 19.39% of Python3 online submissions for Shortest Palindrome.
    """

    def shortestPalindrome(self, s: str) -> str:
        # Reverse the original string
        reversed_string = s[::-1]

        # Combine the original and reversed strings with a separator
        combined_string = s + "#" + reversed_string

        # Build the prefix table for the combined string
        prefix_table = self._build_prefix_table(combined_string)

        # Get the length of the longest palindromic prefix
        palindrome_length = prefix_table[-1]

        # Construct the shortest palindrome by appending the reverse of the suffix
        suffix = reversed_string[: len(s) - palindrome_length]
        return suffix + s

    # Helper function to build the KMP prefix table
    def _build_prefix_table(self, s: str) -> list:
        prefix_table = [0] * len(s)
        length = 0

        # Build the table by comparing characters
        for i in range(1, len(s)):
            while length > 0 and s[i] != s[length]:
                length = prefix_table[length - 1]
            if s[i] == s[length]:
                length += 1
            prefix_table[i] = length
        return prefix_table


class Solution4:
    """
    leetcode solution 4: Rolling Hash Based Algorithm
    Runtime: 68 ms, faster than 57.91% of Python3 online submissions for Shortest Palindrome.
    Memory Usage: 17.1 MB, less than 41.65% of Python3 online submissions for Shortest Palindrome.
    """

    def shortestPalindrome(self, s: str) -> str:
        hash_base = 29
        mod_value = int(1e9 + 7)
        forward_hash = 0
        reverse_hash = 0
        power_value = 1
        palindrome_end_index = -1

        # Calculate rolling hashes and find the longest palindromic prefix
        for i, current_char in enumerate(s):
            # Update forward hash
            forward_hash = (
                forward_hash * hash_base + (ord(current_char) - ord("a") + 1)
            ) % mod_value

            # Update reverse hash
            reverse_hash = (
                reverse_hash + (ord(current_char) - ord("a") + 1) * power_value
            ) % mod_value
            power_value = (power_value * hash_base) % mod_value

            # If forward and reverse hashes match, update palindrome end index
            if forward_hash == reverse_hash:
                palindrome_end_index = i

        # Find the remaining suffix after the longest palindromic prefix
        suffix = s[palindrome_end_index + 1:]

        # Reverse the remaining suffix
        reversed_suffix = suffix[::-1]

        # Prepend the reversed suffix to the original string and return the result
        return reversed_suffix + s


class Solution5:
    """
    leetcode solution 5: Manacher's Algorithm
    Runtime: 147 ms, faster than 39.13% of Python3 online submissions for Shortest Palindrome.
    Memory Usage: 20.4 MB, less than 24.87% of Python3 online submissions for Shortest Palindrome.
    """

    def shortestPalindrome(self, s: str) -> str:
        # Return early if the string is null or empty
        if not s:
            return s

        # Preprocess the string to handle palindromes uniformly
        modified_string = self._preprocess_string(s)
        n = len(modified_string)
        palindrome_radius_array = [0] * n
        center = 0
        right_boundary = 0
        max_palindrome_length = 0

        # Iterate through each character in the modified string
        for i in range(1, n - 1):
            mirror_index = 2 * center - i

            # Use previously computed values to avoid redundant calculations
            if right_boundary > i:
                palindrome_radius_array[i] = min(
                    right_boundary - i, palindrome_radius_array[mirror_index]
                )

            # Expand around the current center while characters match
            while (
                modified_string[i + 1 + palindrome_radius_array[i]]
                == modified_string[i - 1 - palindrome_radius_array[i]]
            ):
                palindrome_radius_array[i] += 1

            # Update the center and right boundary if the palindrome extends beyond the current boundary
            if i + palindrome_radius_array[i] > right_boundary:
                center = i
                right_boundary = i + palindrome_radius_array[i]

            # Update the maximum length of palindrome starting at the beginning
            if i - palindrome_radius_array[i] == 1:
                max_palindrome_length = max(
                    max_palindrome_length, palindrome_radius_array[i]
                )

        # Construct the shortest palindrome by reversing the suffix and prepending it to the original string
        suffix = s[max_palindrome_length:][::-1]
        return suffix + s

    def _preprocess_string(self, s: str) -> str:
        # Add boundaries and separators to handle palindromes uniformly
        return "^" + "#" + "#".join(s) + "#$"


sol = Solution3()
tests = [
    ("aacecaaa", "aaacecaaa"),
    ("abcd", "dcbabcd"),
]
for inp, exp in tests:
    res = sol.shortestPalindrome(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
