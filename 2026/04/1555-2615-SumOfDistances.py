"""
Leetcode
2026-04-23
2615. Sum of Distances
Medium

You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

 

Example 1:

Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

Example 2:

Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.

 

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9

 

Note: This question is the same as 2121: Intervals Between Identical Elements.


Hint 1
Can we use the prefix sum here?
Hint 2
For each number x, collect all the indices where x occurs, and calculate the prefix sum of the array.
Hint 3
For each occurrence of x, the indices to the right will be regular subtraction while the indices to the left will be reversed subtraction.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Time Limit Exceeded
    1065 / 1068 testcases passed
    """

    def distance(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        idxs = defaultdict(list)

        for i, num in enumerate(nums):
            idxs[num].append(i)

        for i, num in enumerate(nums):
            for j in idxs[num]:
                ans[i] += abs(i - j)

        return ans


class Solution1:
    """
    leetcode solution: Grouping + Prefix Sum
    Runtime 112ms Beats 90.94%
    Memory 54.81MB Beats 59.45%
    """

    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
        res = [0] * n
        for group in groups.values():
            total = sum(group)
            prefix_total = 0
            sz = len(group)
            for i, idx in enumerate(group):
                res[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                prefix_total += idx
        return res
