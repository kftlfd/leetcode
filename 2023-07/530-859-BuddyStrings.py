"""
Leetcode
859. Buddy Strings (easy)
2023-07-03

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Constraints:

    1 <= s.length, goal.length <= 2 * 104
    s and goal consist of lowercase letters.
"""


class Solution:
    """
    Wrong answer
    """

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        chars_s = {}
        dif_s = set()
        dif_goal = set()

        for c_s, c_goal in zip(s, goal):
            chars_s[c_s] = chars_s.get(c_s, 0) + 1
            if c_s != c_goal:
                dif_s.add(c_s)
                dif_goal.add(c_goal)

        if len(dif_s) == 0:
            return any(x >= 2 for x in chars_s.values())

        return len(dif_s) == 2 and dif_s == dif_goal


class Solution1:
    """
    leetcode solution
    Time: O(n)
    Space: O(1)
    Runtime: 43 ms, faster than 90.00% of Python3 online submissions for Buddy Strings.
    Memory Usage: 16.5 MB, less than 66.33% of Python3 online submissions for Buddy Strings.
    """

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # if we have 2 same characters in 's' we can swap them
            # and still the strings will remain equal
            freq = [0] * 26
            for c in s:
                if freq[ord(c) - ord('a')] == 1:
                    return True
                freq[ord(c) - ord('a')] += 1
            return False

        idx1 = -1
        idx2 = -1

        for i, (c_s, c_g) in enumerate(zip(s, goal)):
            if c_s != c_g:
                if idx1 == -1:
                    idx1 = i
                elif idx2 == -1:
                    idx2 = i
                else:
                    # we have at least 3 ideces with different characters
                    # thus, we can never make the strings equal with only one swap
                    return False

        if idx2 == -1:
            # we can't swap if the characters at only one index is different
            return False

        return s[idx1] == goal[idx2] and s[idx2] == goal[idx1]


sol = Solution1()
tests = [
    (("abab", "baba"),
     False),

    (("ab", "ba"),
     True),

    (("ab", "ab"),
     False),

    (("aa", "aa"),
     True),
]
for inp, exp in tests:
    res = sol.buddyStrings(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
