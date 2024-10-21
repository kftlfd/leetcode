"""
Leetcode
2024-10-21
1593. Split a String Into the Max Number of Unique Substrings
Medium

Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

 

Constraints:
    - 1 <= s.length <= 16
    - s contains only lower case English letters.
"""


class Solution:
    """
    Wrong Answer
    """

    def maxUniqueSplit(self, s: str) -> int:
        subs = {}
        n = len(s)
        left, right = 0, 1

        while right <= n:
            sub_s = s[left:right]

            if sub_s not in subs:
                subs[sub_s] = left
                left, right = right, right + 1
                continue

            while sub_s in subs and right < n:
                right += 1
                sub_s = s[left:right]

            if sub_s not in subs:
                subs[sub_s] = left
                left, right = right, right + 1
                continue

            # reached end but final sub_s is still in subs
            # get back to previous occurence of sub_s
            prev_left = subs.pop(sub_s)
            left = prev_left
            right = left + len(sub_s) + 1
            # also remove substrings after the prev sub_s
            for k, v in subs.copy().items():
                if v >= left:
                    del subs[k]

        print(subs)
        return len(subs)


class Solution1:
    """
    leetcode solution 1: Backtracking
    Runtime: 155 ms, faster than 91.48% of Python3 online submissions for Split a String Into the Max Number of Unique Substrings.
    Memory Usage: 16.7 MB, less than 19.96% of Python3 online submissions for Split a String Into the Max Number of Unique Substrings.
    """

    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backtrack(s, 0, seen)

    def backtrack(self, s, start, seen):
        if start == len(s):
            return 0

        max_count = 0

        for end in range(start + 1, len(s) + 1):
            sub_string = s[start:end]
            if sub_string not in seen:
                seen.add(sub_string)
                max_count = max(max_count, 1 + self.backtrack(s, end, seen))
                seen.remove(sub_string)

        return max_count


class Solution2:
    """
    leetcode solution 2: Backtracking with Pruning
    Runtime: 7 ms, faster than 100.00% of Python3 online submissions for Split a String Into the Max Number of Unique Substrings.
    Memory Usage: 16.6 MB, less than 19.96% of Python3 online submissions for Split a String Into the Max Number of Unique Substrings.
    """

    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        max_count = [0]
        self.backtrack(s, 0, seen, 0, max_count)
        return max_count[0]

    def backtrack(
        self, s: str, start: int, seen: set, count: int, max_count: list
    ) -> None:
        if count + (len(s) - start) <= max_count[0]:
            return
        if start == len(s):
            max_count[0] = max(max_count[0], count)
            return
        for end in range(start + 1, len(s) + 1):
            sub_string = s[start:end]
            if sub_string not in seen:
                seen.add(sub_string)
                self.backtrack(s, end, seen, count + 1, max_count)
                seen.remove(sub_string)
        return


sol = Solution()
tests = [
    ("wwwzfvedwfvhsww",
     11),

    ('aba',
     2),

    ('ababccc',
     5),

    ('aa',
     1),
]
for inp, exp in tests:
    res = sol.maxUniqueSplit(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
