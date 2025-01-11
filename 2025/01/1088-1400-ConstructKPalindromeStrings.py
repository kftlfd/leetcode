"""
Leetcode
2025-01-11
1400. Construct K Palindrome Strings
Medium

Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

 

Constraints:

    1 <= s.length <= 10^5
    s consists of lowercase English letters.
    1 <= k <= 10^5
"""


from collections import Counter


class Solution:
    """
    Runtime 30ms Beats 74.89%
    Memory 18.04MB Beats 34.36%
    """

    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k >= sum(n % 2 for n in Counter(s).values())


class Solution2:
    """
    leetcode solution 2: Bit Manipulation
    Runtime 53ms Beats 22.03%
    Memory 18.13MB Beats 16.30%
    """

    def canConstruct(self, s: str, k: int) -> bool:
        # Handle edge cases
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        # Initialize oddCount as an integer bitmask
        odd_count = 0

        # Update the bitmask for each character in the string
        for char in s:
            odd_count ^= 1 << (ord(char) - ord("a"))
        # Return if the number of odd frequencies is less than or equal to
        return bin(odd_count).count("1") <= k
