"""
Leetcode
2610. Convert an Array Into a 2D Array With Conditions
Medium
2024-01-02

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

    The 2D array should contain only the elements of the array nums.
    Each row in the 2D array contains distinct integers.
    The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

 

Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.

Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.

 

Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= nums.length
"""

from collections import Counter, deque
from typing import List


class Solution:
    """
    Runtime: 81 ms, faster than 5.01% of Python3 online submissions for Convert an Array Into a 2D Array With Conditions.
    Memory Usage: 17.4 MB, less than 5.17% of Python3 online submissions for Convert an Array Into a 2D Array With Conditions.
    """

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        q = deque([(num, left) for num, left in Counter(nums).items()])

        ans = []

        while q:
            nxt_q = deque()
            arr = []

            for num, left in q:
                if left > 0:
                    arr.append(num)
                if left > 1:
                    nxt_q.append((num, left - 1))

            ans.append(arr)
            q = nxt_q

        return ans


class Solution1:
    """
    leetcode solution
    https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/solution/2192761
    Runtime: 117 ms, faster than 5.01% of Python3 online submissions for Convert an Array Into a 2D Array With Conditions.
    Memory Usage: 17.4 MB, less than 12.28% of Python3 online submissions for Convert an Array Into a 2D Array With Conditions.
    """

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = [0] * (len(nums) + 1)
        ans = []

        for num in nums:
            if cnt[num] >= len(ans):
                ans.append([])
            ans[cnt[num]].append(num)
            cnt[num] += 1

        return ans
