"""
Leetcode
330. Patching Array
Hard
2024-06-16

Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

 

Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].

Example 3:

Input: nums = [1,2,2], n = 5
Output: 0

 

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 10^4
    nums is sorted in ascending order.
    1 <= n <= 2^31 - 1
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/patching-array/discuss/78488/Solution-+-explanation
    https://leetcode.com/problems/patching-array/discuss/1432422/Python-2-solutions:-merge-intervals-+-greedy-explained
    Runtime: 47 ms, faster than 94.76% of Python3 online submissions for Patching Array.
    Memory Usage: 16.6 MB, less than 69.93% of Python3 online submissions for Patching Array.
    """

    def minPatches(self, nums: List[int], n: int) -> int:
        can_reach = 0
        patches = 0
        i = 0
        l = len(nums)

        while can_reach < n:
            if i < l and nums[i] <= can_reach + 1:
                can_reach += nums[i]
                i += 1
            else:
                patches += 1
                can_reach += can_reach + 1

        return patches
