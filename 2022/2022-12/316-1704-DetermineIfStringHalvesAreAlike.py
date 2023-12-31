"""
Leetcode
1704. Determine if String Halves Are Alike (easy)
2022-12-01

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
"""

from typing import List, Optional


# Runtime: 77 ms, faster than 29.60% of Python3 online submissions for Determine if String Halves Are Alike.
# Memory Usage: 13.7 MB, less than 98.54% of Python3 online submissions for Determine if String Halves Are Alike.
class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        half = len(s) // 2
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        count = 0

        for c in s[:half]:
            if c in vowels:
                count += 1

        for c in s[half:]:
            if c not in vowels:
                continue
            if count == 0:
                return False
            count -= 1

        return count == 0


# https://leetcode.com/problems/determine-if-string-halves-are-alike/discuss/1146585/Python-short-O(n)-solution-explained
# Runtime: 75 ms, faster than 34.41% of Python3 online submissions for Determine if String Halves Are Alike.
# Memory Usage: 13.9 MB, less than 77.72% of Python3 online submissions for Determine if String Halves Are Alike.
class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        s = s.lower()
        half = len(s) // 2
        vowels = set("aeiou")

        return sum(c in vowels for c in s[:half]) == sum(c in vowels for c in s[half:])


s = Solution()
tests = [
    ("book",
     True),

    ("textbook",
     False),
]
for inp, exp in tests:
    res = s.halvesAreAlike(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
