"""
Leetcode
409. Longest Palindrome
Easy
2024-06-04

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

 

Constraints:

    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.
"""

from collections import Counter


class Solution:
    """
    Runtime: 38 ms, faster than 49.08% of Python3 online submissions for Longest Palindrome.
    Memory Usage: 16.5 MB, less than 98.44% of Python3 online submissions for Longest Palindrome.
    """

    def longestPalindrome(self, s: str) -> int:
        ans = 0
        has_odd = 0

        for _, n in Counter(s).most_common():
            if n + 1 == n ^ 1:
                # is_even
                ans += n
            else:
                ans += n - has_odd
                has_odd = 1

        return ans


class Solution2:
    """
    leetcode solution 2: Greedy Way (Optimized)
    Runtime: 33 ms, faster than 80.51% of Python3 online submissions for Longest Palindrome.
    Memory Usage: 16.7 MB, less than 34.50% of Python3 online submissions for Longest Palindrome.
    """

    def longestPalindrome(self, s: str) -> int:
        odd_freq_chars_count = 0
        frequency_map = {}

        # Loop over the string
        for c in s:
            # Update count of current character
            frequency_map[c] = frequency_map.get(c, 0) + 1

            # If the current frequency of the character is odd,
            # increment odd_freq_chars_count
            if frequency_map[c] % 2 == 1:
                odd_freq_chars_count += 1
            else:
                odd_freq_chars_count -= 1

        # If there are characters with odd frequencies, we are
        # guaranteed to have at least one letter left unmatched,
        # which can make the center of an odd length palindrome.
        if odd_freq_chars_count > 0:
            return len(s) - odd_freq_chars_count + 1
        else:
            return len(s)


class Solution3:
    """
    leetcode solution 3: Greedy Way (Hash Set)
    Runtime: 34 ms, faster than 76.19% of Python3 online submissions for Longest Palindrome.
    Memory Usage: 16.6 MB, less than 80.97% of Python3 online submissions for Longest Palindrome.
    """

    def longestPalindrome(self, s: str) -> int:
        character_set = set()
        res = 0

        # Loop over characters in the string
        for c in s:
            # If set contains the character, match found
            if c in character_set:
                character_set.remove(c)
                # Add the two occurrences to our palindrome
                res += 2
            else:
                # Add the character to the set
                character_set.add(c)

        # If any character remains, we have at least one unmatched
        # character to make the center of an odd length palindrome.
        if character_set:
            res += 1

        return res
