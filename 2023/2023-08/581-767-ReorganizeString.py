"""
Leetcode
767. Reorganize String (medium)
2023-08-23

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"

Example 2:

Input: s = "aaab"
Output: ""

Constraints:

    1 <= s.length <= 500
    s consists of lowercase English letters.
"""


from collections import Counter
from heapq import heappush, heappop, heapify


class Solution:
    """
    Runtime: 33 ms, faster than 96.12% of Python3 online submissions for Reorganize String.
    Memory Usage: 16.4 MB, less than 46.15% of Python3 online submissions for Reorganize String.
    """

    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        pq = []
        for c, freq in cnt.items():
            heappush(pq, (-freq, c))

        ans = []
        while pq:
            freq, c = heappop(pq)

            if not ans or c != ans[-1]:
                ans.append(c)
                if freq < -1:
                    heappush(pq, (freq + 1, c))
                continue

            if not pq:
                break

            freq2, c2 = heappop(pq)
            ans.append(c2)
            heappush(pq, (freq, c))
            if freq2 < -1:
                heappush(pq, (freq2 + 1, c2))

        if len(ans) != len(s):
            return ""

        return "".join(ans)


class Solution1:
    """
    leetcode solution 1: Counting and Priority Queue
    Time: O(n * log(k)) -- n = len(s), k = len(set(s))
    Space: O(k)
    """

    def reorganizeString(self, s: str) -> str:
        ans = []
        # Min heap ordered by character counts, so we will use
        # negative values for count
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)

        while pq:
            count_first, char_first = heappop(pq)
            if not ans or char_first != ans[-1]:
                ans.append(char_first)
                if count_first + 1 != 0:
                    heappush(pq, (count_first + 1, char_first))
            else:
                if not pq:
                    return ''
                count_second, char_second = heappop(pq)
                ans.append(char_second)
                if count_second + 1 != 0:
                    heappush(pq, (count_second + 1, char_second))
                heappush(pq, (count_first, char_first))

        return ''.join(ans)


class Solution2:
    """
    leetcode solution 2: Counting and Odd/Even
    Time: O(n)
    Space: O(k)
    Runtime: 44 ms, faster than 64.10% of Python3 online submissions for Reorganize String.
    Memory Usage: 16.2 MB, less than 96.85% of Python3 online submissions for Reorganize String.
    """

    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)
        max_count = 0
        letter = ''
        for char, count in char_counts.items():
            if count > max_count:
                max_count = count
                letter = char

        if max_count > (len(s) + 1) // 2:
            return ''

        ans = [''] * len(s)
        index = 0

        # place the most frequent letter
        while char_counts[letter] != 0:
            ans[index] = letter
            index += 2
            char_counts[letter] -= 1

        # place rest of the letters in any order
        for char, count in char_counts.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1

        return ''.join(ans)


sol = Solution2()
tests = [
    ('aab',
     'aba'),

    ('aaab',
     ''),
]
for inp, exp in tests:
    res = sol.reorganizeString(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
