"""
Leetcode
1456. Maximum Number of Vowels in a Substring of Given Length (medium)
2023-05-05

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""


class Solution1:
    """
    Runtime: 243 ms, faster than 31.41% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    Memory Usage: 17.4 MB, less than 5.01% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    """

    def maxVowels(self, s: str, k: int) -> int:

        vowels = ['a', 'e', 'i', 'o', 'u']
        curr_vowels = 0

        for c in s[:k]:
            if c in vowels:
                curr_vowels += 1

        max_vowels = curr_vowels

        l = 0
        r = k - 1

        while r < len(s) - 1:
            l += 1
            r += 1
            if s[l-1] in vowels:
                curr_vowels -= 1
            if s[r] in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)

        return max_vowels


class Solution2:
    """
    Runtime: 224 ms, faster than 39.30% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    Memory Usage: 17.2 MB, less than 14.59% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    """

    def maxVowels(self, s: str, k: int) -> int:

        vowels = {
            'a': 1,
            'e': 1,
            'i': 1,
            'o': 1,
            'u': 1,
        }

        curr_vowels = 0

        for c in s[:k]:
            if c in vowels:
                curr_vowels += 1

        max_vowels = curr_vowels

        l = 0
        r = k - 1

        while r < len(s) - 1:
            l += 1
            r += 1
            if vowels.get(s[l-1], 0) == 1:
                curr_vowels -= 1
            if vowels.get(s[r], 0) == 1:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)

        return max_vowels


class Solution3:
    """
    leetcode solution
    Runtime: 232 ms, faster than 35.99% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    Memory Usage: 17.3 MB, less than 14.59% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    """

    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Build the window of size k, count the number of vowels it contains.
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count

        if answer == k:
            return answer

        # Slide the window to the right, focus on the added character and the
        # removed character and update "count". Record the largest "count".
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)

        return answer


sol = Solution3()
tests = [
    (("weallloveyou", 7),
     4),

    (("abciiidef", 3),
     3),

    (("aeiou", 2),
     2),

    (("leetcode", 3),
     2),
]
for inp, exp in tests:
    res = sol.maxVowels(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
