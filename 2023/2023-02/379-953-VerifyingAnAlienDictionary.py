"""
Leetcode
953. Verifying an Alien Dictionary (easy)
2023-02-02

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""

from typing import List, Optional


class Solution:
    """
    leetcode solution
    Runtime: 30 ms, faster than 96.70% of Python3 online submissions for Verifying an Alien Dictionary.
    Memory Usage: 13.9 MB, less than 77.53% of Python3 online submissions for Verifying an Alien Dictionary.
    """

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alphabet = {}
        for i, c in enumerate(order):
            alphabet[c] = i

        for i in range(len(words) - 1):
            cur = words[i]
            nxt = words[i + 1]

            for j in range(len(cur)):
                if j >= len(nxt) or alphabet[cur[j]] > alphabet[nxt[j]]:
                    return False
                if alphabet[cur[j]] < alphabet[nxt[j]]:
                    break

        return True


s = Solution()
tests = [
    ((["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"),
     True),

    ((["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"),
     False),

    ((["apple", "app"], "abcdefghijklmnopqrstuvwxyz"),
     False)
]
for inp, exp in tests:
    res = s.isAlienSorted(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
