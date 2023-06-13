"""
Leetcode
2352. Equal Row and Column Pairs (medium)
2023-06-13

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 200
    1 <= grid[i][j] <= 10^5
"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    """
    Runtime: 526 ms, faster than 55.51% of Python3 online submissions for Equal Row and Column Pairs.
    Memory Usage: 22 MB, less than 13.34% of Python3 online submissions for Equal Row and Column Pairs.
    """

    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        ht = defaultdict(list)

        for i, row in enumerate(grid):
            row_vals = tuple(v for v in row)
            ht[row_vals].append(i)

        for col in range(n):
            col_vals = tuple(grid[row][col] for row in range(n))
            ans += len(ht[col_vals])

        return ans


class Solution1:
    """
    leetcode solution: Hash Map
    Runtime: 559 ms, faster than 46.91% of Python3 online submissions for Equal Row and Column Pairs.
    Memory Usage: 21.7 MB, less than 51.03% of Python3 online submissions for Equal Row and Column Pairs.
    """

    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        # Keep track of the frequency of each row.
        row_counter = Counter(tuple(row) for row in grid)

        # Add up the frequency of each column in map.
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]

        return count


class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, array):
        my_trie = self.trie
        for a in array:
            if a not in my_trie.children:
                my_trie.children[a] = TrieNode()
            my_trie = my_trie.children[a]
        my_trie.count += 1

    def search(self, array):
        my_trie = self.trie
        for a in array:
            if a in my_trie.children:
                my_trie = my_trie.children[a]
            else:
                return 0
        return my_trie.count


class Solution2:
    """
    leetcode solution: Trie
    Runtime: 726 ms, faster than 21.16% of Python3 online submissions for Equal Row and Column Pairs.
    Memory Usage: 32.3 MB, less than 5.10% of Python3 online submissions for Equal Row and Column Pairs.
    """

    def equalPairs(self, grid: List[List[int]]) -> int:
        my_trie = Trie()
        count = 0
        n = len(grid)

        for row in grid:
            my_trie.insert(row)

        for c in range(n):
            col_array = [grid[i][c] for i in range(n)]
            count += my_trie.search(col_array)

        return count


s = Solution()
tests = [
    ([[3, 2, 1], [1, 7, 6], [2, 7, 7]],
     1),

    ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]],
     3),
]
for inp, exp in tests:
    res = s.equalPairs(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
