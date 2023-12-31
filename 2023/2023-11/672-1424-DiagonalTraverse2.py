"""
Leetcode
1424. Diagonal Traverse II (medium)
2023-11-22

Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

 

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i].length <= 10^5
    1 <= sum(nums[i].length) <= 10^5
    1 <= nums[i][j] <= 10^5

Hints:
- Notice that numbers with equal sums of row and column indexes belong to the same diagonal.
- Store them in tuples (sum, row, val), sort them, and then regroup the answer.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Runtime: 788 ms, faster than 62.08% of Python3 online submissions for Diagonal Traverse II.
    Memory Usage: 38.5 MB, less than 68.27% of Python3 online submissions for Diagonal Traverse II.
    """

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = [(r + c, -r, val)
                  for r, row in enumerate(nums)
                  for c, val in enumerate(row)]
        return [n[2] for n in sorted(groups)]


class Solution1:
    """
    leetcode solution 1: Group Elements by the Sum of Row and Column Indices
    Runtime: 789 ms, faster than 59.75% of Python3 online submissions for Diagonal Traverse II.
    Memory Usage: 41.5 MB, less than 21.98% of Python3 online submissions for Diagonal Traverse II.
    """

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])

        ans = []
        curr = 0

        while curr in groups:
            ans.extend(groups[curr])
            curr += 1

        return ans


class Solution2:
    """
    leetcode solution 2: Breadth First Search
    Runtime: 762 ms, faster than 92.14% of Python3 online submissions for Diagonal Traverse II.
    Memory Usage: 38.1 MB, less than 70.52% of Python3 online submissions for Diagonal Traverse II.
    """

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = deque([(0, 0)])
        ans = []

        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))

            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))

        return ans


s = Solution()
tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
     [1, 4, 2, 7, 5, 3, 8, 6, 9]),

    ([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]],
     [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]),
]
for inp, exp in tests:
    res = s.findDiagonalOrder(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
