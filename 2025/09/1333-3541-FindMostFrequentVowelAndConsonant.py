"""
Leetcode
2025-09-13
3541. Find Most Frequent Vowel and Consonant
Easy

You are given a string s consisting of lowercase English letters ('a' to 'z').

Your task is to:

    Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
    Find the consonant (all other letters excluding vowels) with the maximum frequency.

Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
The frequency of a letter x is the number of times it occurs in the string.

 

Example 1:

Input: s = "successes"

Output: 6

Explanation:

    The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
    The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
    The output is 2 + 4 = 6.

Example 2:

Input: s = "aeiaeia"

Output: 3

Explanation:

    The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
    There are no consonants in s. Hence, maximum consonant frequency = 0.
    The output is 3 + 0 = 3.

 

Constraints:

    1 <= s.length <= 100
    s consists of lowercase English letters only.


Hint 1
Use a hashmap
Hint 2
Simulate as described
"""

from collections import Counter


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.71MB Beats 63.40%
    """

    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"

        cnt_vowels = {c: 0 for c in vowels}
        cnt_consonants = {"b": 0}

        for c in s:
            if c in vowels:
                cnt_vowels[c] += 1
            else:
                cnt_consonants[c] = cnt_consonants.get(c, 0) + 1

        return max(cnt_vowels.values()) + max(cnt_consonants.values())


class Solution1:
    """
    leetcode solution
    Runtime 2ms Beats 72.45%
    Memory 17.80MB Beats 63.40%
    """

    def maxFreqSum(self, s: str) -> int:
        mp = Counter(s)
        vowel = max((mp[ch] for ch in mp if ch in "aeiou"), default=0)
        consonant = max((mp[ch] for ch in mp if ch not in "aeiou"), default=0)
        return vowel + consonant
