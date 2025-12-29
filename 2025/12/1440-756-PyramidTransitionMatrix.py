"""
Leetcode
2025-12-29
756. Pyramid Transition Matrix
Medium

You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

    For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.

You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

 

Example 1:

Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
Output: true
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.

Example 2:

Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
Output: false
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.

 

Constraints:

    2 <= bottom.length <= 6
    0 <= allowed.length <= 216
    allowed[i].length == 3
    The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
    All the values of allowed are unique.


"""

from collections import defaultdict
from typing import List


class Solution00:
    """
    Runtime 9856ms Beats 5.45%
    Memory 17.64MB Beats 94.06%
    """

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        blocks = {"A", "B", "C", "D", "E", "F"}
        allowed_set = set()
        for tr in allowed:
            allowed_set.add(tr)

        grid = [[""] * len(bottom) for _ in range(len(bottom) + 1)]
        grid[len(bottom)] = list(bottom)

        def dfs(grid: List[List[str]], curRow: int, curCol: int) -> bool:
            if curRow == 0:
                return True

            nxtRow = curRow
            nxtCol = curCol + 1
            if nxtCol == curRow:
                nxtRow = curRow - 1
                nxtCol = 0

            prev = grid[curRow+1][curCol] + grid[curRow+1][curCol+1]

            for b in blocks:
                if prev + b in allowed_set:
                    grid[curRow][curCol] = b
                    if dfs(grid, nxtRow, nxtCol):
                        return True

            return False

        return dfs(grid, len(bottom) - 1, 0)


class Solution01:
    """
    Runtime 3727ms Beats 45.05%
    Memory 17.35MB Beats 98.02%
    """

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_hm = defaultdict(list)
        for tr in allowed:
            allowed_hm[tr[:2]].append(tr[2])

        grid = [[""] * len(bottom) for _ in range(len(bottom) + 1)]
        grid[len(bottom)] = list(bottom)

        def dfs(grid: List[List[str]], curRow: int, curCol: int) -> bool:
            if curRow == 0:
                return True

            nxtRow = curRow
            nxtCol = curCol + 1
            if nxtCol == curRow:
                nxtRow = curRow - 1
                nxtCol = 0

            prev = grid[curRow+1][curCol] + grid[curRow+1][curCol+1]

            for b in allowed_hm[prev]:
                grid[curRow][curCol] = b
                if dfs(grid, nxtRow, nxtCol):
                    return True

            return False

        return dfs(grid, len(bottom) - 1, 0)


class Solution2:
    """
    leetcode solution 2: Depth-First Search
    Time Limit Exceeded
    """

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        T = defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        # Comments can be used to cache intermediate results
        # seen = set()
        def solve(A):
            if len(A) == 1:
                return True
            # if A in seen: return False
            # seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i=0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)


class Solution3:
    """
    sample 46ms solution
    Runtime 0ms Beats 100.00%
    Memory 17.40MB Beats 98.02%
    """

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for temp in allowed:
            lr = temp[:2]
            t = temp[2:]
            mp[lr].append(t)
        # line = bottom

        def dfs(line):
            lth = len(line)
            if lth == 1:
                return True
            cand = []
            maxcand = 0
            for i in range(lth-1):
                lr = line[i:i+2]
                if lr not in mp:
                    continue
                toplist = mp[lr]
                cand.append(toplist)
                maxcand = max(maxcand, len(toplist))
            if len(cand) != lth-1:
                return False
            # up = [None] * (lth-1)
            for i in range(maxcand):
                temp = ""
                for j in range(lth-1):
                    idx = min(len(cand[j])-1, i)
                    u = cand[j][idx]
                    # print(cand[j], u)
                    temp += u
                # print(line, temp)
                if len(temp) == lth-1:
                    if dfs(temp):
                        return True
            return False
        return dfs(bottom)
