"""
Leetcode
2025-06-07
3170. Lexicographically Minimum String After Removing Stars
Medium

You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

    Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.

Return the

resulting string after removing all '*' characters.

 

Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.

 

Constraints:

    1 <= s.length <= 10^5
    s consists only of lowercase English letters and '*'.
    The input is generated such that it is possible to delete all '*' characters.

"""

from heapq import heappop, heappush


class Solution:
    """
    Runtime 583ms Beats 58.27%
    Memory 33.83MB Beats 5.04%
    """

    def clearStars(self, s: str) -> str:
        stack = []

        for i, c in enumerate(s):
            if c == "*":
                if stack:
                    heappop(stack)
            else:
                heappush(stack, (c, -i))

        ans = [c for c, i in sorted(stack, key=lambda x: -x[1])]

        return "".join(ans)


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 495ms Beats 78.42%
    Memory 23.35MB Beats 79.14%
    """

    def clearStars(self, s: str) -> str:
        cnt = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            if c != "*":
                cnt[ord(c) - ord("a")].append(i)
            else:
                for j in range(26):
                    if cnt[j]:
                        arr[cnt[j].pop()] = "*"
                        break
        return "".join(c for c in arr if c != "*")
