"""
Leetcode
2025-12-21
955. Delete Columns to Make Sorted II
Medium

You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.

 

Example 1:

Input: strs = ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, strs = ["a", "b", "c"].
Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.

Example 2:

Input: strs = ["xc","yb","za"]
Output: 0
Explanation: 
strs is already in lexicographic order, so we do not need to delete anything.
Note that the rows of strs are not necessarily in lexicographic order:
i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)

Example 3:

Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: We have to delete every column.

 

Constraints:

    n == strs.length
    1 <= n <= 100
    1 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.


"""

from typing import List


class Solution:
    """
    Runtime 4ms Beats 55.13%
    Memory 17.69MB Beats 97.44%
    """

    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        removed_col = [False] * n
        q = [(0, m)]  # (row_start, row_end)

        def is_col_sorted(col: int, row_start: int, row_end: int) -> bool:
            for r in range(row_start + 1, row_end):
                if strs[r-1][col] > strs[r][col]:
                    return False
            return True

        for col in range(n):
            for row_start, row_end in q:
                if not is_col_sorted(col, row_start, row_end):
                    removed_col[col] = True
                    break

            if removed_col[col]:
                continue

            # break into new partitions
            nxt_q = []
            for row_start, row_end in q:
                prev = row_start
                for cur in range(row_start+1, row_end+1):
                    same = cur < m and strs[cur][col] == strs[prev][col]
                    if (not same or cur == m - 1) and cur - prev > 1:
                        nxt_q.append((prev, cur))
                    if not same:
                        prev = cur
            q = nxt_q

        return sum(removed_col)


class Solution1:
    """
    leetcode solution 1: Greedy
    Runtime 11ms Beats 25.64%
    Memory 17.31MB Beats 100.00%
    """

    def minDeletionSize(self, strs: List[str]) -> int:
        def is_sorted(A):
            return all(A[i] <= A[i+1] for i in range(len(A) - 1))

        ans = 0
        # cur : all rows we have written
        # For example, with A = ["abc","def","ghi"] we might have
        # cur = ["ab", "de", "gh"].
        cur = [""] * len(strs)

        for col in zip(*strs):
            # cur2 : What we potentially can write, including the
            #        newest column 'col'.
            # Eg. if cur = ["ab","de","gh"] and col = ("c","f","i"),
            # then cur2 = ["abc","def","ghi"].
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] = cur2[i] + letter

            if is_sorted(cur2):
                cur = cur2
            else:
                ans += 1

        return ans


class Solution2:
    """
    leetcode solution 2: Greedy with Optimizations
    Runtime 7ms Beats 38.46%
    Memory 17.64MB Beats 97.44%
    """

    def minDeletionSize(self, A: List[str]) -> int:
        # cuts[i] is True : we don't need to check col[i] <= col[i+1]
        cuts = [False] * (len(A) - 1)

        ans = 0
        for col in zip(*A):
            if all(cuts[i] or col[i] <= col[i+1] for i in range(len(col) - 1)):
                for i in range(len(col) - 1):
                    if col[i] < col[i+1]:
                        cuts[i] = True
            else:
                ans += 1
        return ans


s = Solution()
tests = [
    (["vdy", "vei", "zvc", "zld"], 2),
    (["xga", "xfb", "yfa"], 1),
    (["zyx", "wvu", "tsr"], 3),
    (["xc", "yb", "za"], 0),
]
for inp, exp in tests:
    res = s.minDeletionSize(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
