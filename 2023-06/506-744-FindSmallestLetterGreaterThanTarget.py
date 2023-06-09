"""
Leetcode
744. Find Smallest Letter Greater Than Target (easy)
2023-06-09

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

Constraints:

    2 <= letters.length <= 104
    letters[i] is a lowercase English letter.
    letters is sorted in non-decreasing order.
    letters contains at least two different characters.
    target is a lowercase English letter.
"""

from typing import List
from bisect import bisect_right


class Solution:
    """
    Runtime: 133 ms, faster than 55.65% of Python3 online submissions for Find Smallest Letter Greater Than Target.
    Memory Usage: 16.7 MB, less than 45.52% of Python3 online submissions for Find Smallest Letter Greater Than Target.
    """

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters) - 1
        target_ord = ord(target)

        left = 0
        right = n

        while left <= right:
            m = (left + right) // 2
            if ord(letters[m]) > target_ord:
                right = m - 1
            else:
                left = m + 1

        return letters[left] if left <= n else letters[0]


class Solution1:
    """
    https://leetcode.com/problems/find-smallest-letter-greater-than-target/solution/1921814
    Runtime: 132 ms, faster than 58.00% of Python3 online submissions for Find Smallest Letter Greater Than Target.
    Memory Usage: 16.9 MB, less than 6.11% of Python3 online submissions for Find Smallest Letter Greater Than Target.
    """

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target) % len(letters)]


s = Solution1()
tests = [
    ((["c", "f", "j"], "a"),
     "c"),

    ((["c", "f", "j"], "c"),
     "f"),

    ((["x", "x", "y", "y"], "z"),
     "x"),
]
for inp, exp in tests:
    res = s.nextGreatestLetter(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
