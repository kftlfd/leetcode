"""
Leetcode
2024-12-17
2182. Construct String With Repeat Limit
Medium

You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

 

Example 1:

Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

Example 2:

Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.

 

Constraints:

    1 <= repeatLimit <= s.length <= 10^5
    s consists of lowercase English letters.
"""


from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    """
    Runtime: 827 ms, faster than 8.70% of Python3 online submissions for Construct String With Repeat Limit.
    Memory Usage: 19.4 MB, less than 22.73% of Python3 online submissions for Construct String With Repeat Limit.
    """

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = [0] * 26
        a = ord("a")
        for c in s:
            count[ord(c) - a] += 1

        ans = []
        last_char = -1
        cur_repeat = 0

        while True:
            char_added = False

            for i in range(25, -1, -1):
                if count[i] < 1 or (last_char == i and cur_repeat >= repeatLimit):
                    continue

                if i != last_char:
                    cur_repeat = 0

                last_char = i
                cur_repeat += 1
                count[i] -= 1
                ans.append(chr(i + a))
                char_added = True
                break

            if not char_added:
                break

        return "".join(ans)


class Solution2:
    """
    leetcode solution 2: Heap-Optimized Greedy Character Frequency Distribution
    Runtime: 191 ms, faster than 81.88% of Python3 online submissions for Construct String With Repeat Limit.
    Memory Usage: 19.9 MB, less than 6.99% of Python3 online submissions for Construct String With Repeat Limit.
    """

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapify(max_heap)
        result = []

        while max_heap:
            char_neg, count = heappop(max_heap)
            char = chr(-char_neg)
            use = min(count, repeatLimit)
            result.append(char * use)

            if count > use and max_heap:
                next_char_neg, next_count = heappop(max_heap)
                result.append(chr(-next_char_neg))
                if next_count > 1:
                    heappush(max_heap, (next_char_neg, next_count - 1))
                heappush(max_heap, (char_neg, count - use))

        return "".join(result)
