"""
Leetcode
2026-08-13
2213. Longest Substring of One Repeating Character
Hard

You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

 

Example 1:

Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation: 
- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc". 
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].

Example 2:

Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].

 

Constraints:

    1 <= s.length <= 10^5
    s consists of lowercase English letters.
    k == queryCharacters.length == queryIndices.length
    1 <= k <= 10^5
    queryCharacters consists of lowercase English letters.
    0 <= queryIndices[i] < s.length


Hint 1
Use a segment tree to perform fast point updates and range queries.
Hint 2
We need each segment tree node to store the length of the longest substring of that segment consisting of only 1 repeating character.
Hint 3
We will also have each segment tree node store the leftmost and rightmost character of the segment, the max length of a prefix substring consisting of only 1 repeating character, and the max length of a suffix substring consisting of only 1 repeating character.
Hint 4
Use this information to properly merge the two segment tree nodes together.
"""

from typing import List

from sortedcontainers import SortedList


class Solution1:
    """
    leetcode solution 1: Segment Tree
    Runtime 3408ms Beats 39.35%
    Memory 109.37MB Beats 22.95%
    """

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        pre = [0] * (4 * n)
        suf = [0] * (4 * n)
        maxLen = [0] * (4 * n)
        leftChar = [""] * (4 * n)
        rightChar = [""] * (4 * n)

        def build(u: int, l: int, r: int) -> None:
            if l == r:
                pre[u] = 1
                suf[u] = 1
                maxLen[u] = 1
                leftChar[u] = s[l]
                rightChar[u] = s[l]
                return
            mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)
            pushUp(u, l, r)

        def pushUp(u: int, l: int, r: int) -> None:
            mid = (l + r) >> 1
            leftLen = mid - l + 1
            rightLen = r - mid
            left = u << 1
            right = u << 1 | 1
            leftChar[u] = leftChar[left]
            rightChar[u] = rightChar[right]
            pre[u] = pre[left]
            if pre[left] == leftLen and rightChar[left] == leftChar[right]:
                pre[u] = pre[left] + pre[right]
            suf[u] = suf[right]
            if suf[right] == rightLen and rightChar[left] == leftChar[right]:
                suf[u] = suf[right] + suf[left]
            maxLen[u] = max(maxLen[left], maxLen[right])
            if rightChar[left] == leftChar[right]:
                maxLen[u] = max(maxLen[u], suf[left] + pre[right])

        def update(u: int, l: int, r: int, pos: int, ch: str) -> None:
            if l == r:
                leftChar[u] = ch
                rightChar[u] = ch
                return
            mid = (l + r) >> 1
            if pos <= mid:
                update(u << 1, l, mid, pos, ch)
            else:
                update(u << 1 | 1, mid + 1, r, pos, ch)
            pushUp(u, l, r)

        build(1, 0, n - 1)
        k = len(queryIndices)
        ans = []
        for i in range(k):
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans.append(maxLen[1])
        return ans


class Solution2:
    """
    leetcode solution 2: Ordered Set Simulating Interval Merging
    Runtime 2049ms Beats 80.33%
    Memory 41.52MB Beats 98.36%
    """

    def longestRepeating(self, sstr: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(sstr)
        s = list(sstr)
        segs = SortedList()
        lens = SortedList()

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segs.add((i, j - 1))
            lens.add(j - i)
            i = j

        k = len(queryIndices)
        ans = []

        for q in range(k):
            pos = queryIndices[q]
            ch = queryCharacters[q]

            if s[pos] != ch:
                idx = segs.bisect_right((pos, n)) - 1
                L, R = segs[idx]
                segs.pop(idx)
                lens.remove(R - L + 1)

                if L <= pos - 1:
                    segs.add((L, pos - 1))
                    lens.add(pos - L)
                if pos + 1 <= R:
                    segs.add((pos + 1, R))
                    lens.add(R - pos)

                newL, newR = pos, pos

                if pos + 1 < n and s[pos + 1] == ch:
                    idx2 = segs.bisect_left((pos + 1, -1))
                    if idx2 < len(segs) and segs[idx2][0] == pos + 1:
                        rightL, rightR = segs[idx2]
                        lens.remove(rightR - rightL + 1)
                        newR = rightR
                        segs.pop(idx2)

                if pos > 0 and s[pos - 1] == ch:
                    idx3 = segs.bisect_right((pos - 1, n)) - 1
                    if idx3 >= 0 and segs[idx3][1] == pos - 1:
                        leftL, leftR = segs[idx3]
                        lens.remove(leftR - leftL + 1)
                        newL = leftL
                        segs.pop(idx3)

                segs.add((newL, newR))
                lens.add(newR - newL + 1)
                s[pos] = ch

            ans.append(lens[-1])

        return ans
