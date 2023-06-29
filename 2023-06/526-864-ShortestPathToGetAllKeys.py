"""
Leetcode
864. Shortest Path to Get All Keys (hard)
2023-06-29

You are given an m x n grid grid where:

    '.' is an empty cell.
    '#' is a wall.
    '@' is the starting point.
    Lowercase letters represent keys.
    Uppercase letters represent locks.

You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:

Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.

Example 2:

Input: grid = ["@..aA","..B#.","....b"]
Output: 6

Example 3:

Input: grid = ["@Aa"]
Output: -1

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 30
    grid[i][j] is either an English letter, '.', '#', or '@'.
    The number of keys in the grid is in the range [1, 6].
    Each key in the grid is unique.
    Each key in the grid has a matching lock.
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    """
    leetcode solution: BFS
    Time: O(m * n * 2^k)
    Space: O(m * n * 2^k)
    Runtime: 267 ms, faster than 95.21% of Python3 online submissions for Shortest Path to Get All Keys.
    Memory Usage: 20 MB, less than 93.29% of Python3 online submissions for Shortest Path to Get All Keys.
    """

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])

        # seen['key'] is only for BFS with key state equals 'keys'
        seen = defaultdict(set)

        def key(cell: str) -> int:
            return 1 << (ord(cell) - ord('a'))

        def lock(cell: str) -> int:
            return 1 << (ord(cell) - ord('A'))

        key_set = set()
        lock_set = set()
        all_keys = 0
        start_r = -1
        start_c = -1
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]

                if cell in 'abcdef':
                    all_keys += key(cell)
                    key_set.add(cell)

                if cell in 'ABCDEF':
                    lock_set.add(cell)

                if cell == '@':
                    start_r = i
                    start_c = j

        # [row, col, key_state, steps]
        q = deque([(start_r, start_c, 0, 0)])
        seen[0].add((start_r, start_c))

        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

        while q:
            cur_r, cur_c, keys, steps = q.popleft()
            for dr, dc in moves:
                nxt_r, nxt_c = cur_r + dr, cur_c + dc

                # if cell is unreachable, continue
                if not (0 <= nxt_r < m and 0 <= nxt_c < n and grid[nxt_r][nxt_c] != '#'):
                    continue

                cell = grid[nxt_r][nxt_c]

                # if it is a key we haven't picked up yet
                if cell in key_set and not key(cell) & keys:
                    new_keys = keys | key(cell)

                    # if we collect all keys, return steps+1
                    if new_keys == all_keys:
                        return steps + 1

                    # otherwise, just add this state to seen and q
                    seen[new_keys].add((nxt_r, nxt_c))
                    q.append((nxt_r, nxt_c, new_keys, steps+1))

                # if it is a lock and we don't have its key, continue
                elif cell in lock_set and not keys & lock(cell):
                    continue

                # we can walk to this cell if we haven't been here before
                # with the same key state
                elif (nxt_r, nxt_c) not in seen[keys]:
                    seen[keys].add((nxt_r, nxt_c))
                    q.append((nxt_r, nxt_c, keys, steps + 1))

        return -1


s = Solution()
tests = [
    (["@.a..", "###.#", "b.A.B"],
     8),

    (["@..aA", "..B#.", "....b"],
     6),

    (["@Aa"],
     -1),
]
for inp, exp in tests:
    res = s.shortestPathAllKeys(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
