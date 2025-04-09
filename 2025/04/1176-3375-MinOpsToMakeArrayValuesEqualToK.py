"""
Leetcode
2025-04-09
3375. Minimum Operations to Make Array Values Equal to K
Easy

You are given an integer array nums and an integer k.

An integer h is called valid if all values in the array that are strictly greater than h are identical.

For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.

You are allowed to perform the following operation on nums:

    Select an integer h that is valid for the current values in nums.
    For each index i where nums[i] > h, set nums[i] to h.

Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.

 

Example 1:

Input: nums = [5,2,5,4,5], k = 2

Output: 2

Explanation:

The operations can be performed in order using valid integers 4 and then 2.

Example 2:

Input: nums = [2,1,2], k = 2

Output: -1

Explanation:

It is impossible to make all the values equal to 2.

Example 3:

Input: nums = [9,7,5,3], k = 1

Output: 4

Explanation:

The operations can be performed using valid integers in the order 7, 5, 3, and 1.

 

Constraints:

    1 <= nums.length <= 100 
    1 <= nums[i] <= 100
    1 <= k <= 100


Hint 1
Handle the case when the array contains an integer less than k
Hint 2
Start by performing operations on the highest integer
Hint 3
You can perform an operation on the highest integer using the second-highest, an operation on the second-highest using the third-highest, and so forth.
Hint 4
The answer is the number of distinct integers in the array that are larger than k.
"""

from typing import List


class Solution:
    """
    Runtime 72ms Beats 23.82%
    Memory 17.87MB Beats 35.61%
    """

    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1

        vals = set(nums)
        vals.add(k)
        ops = 0

        for val in sorted(vals, reverse=True):
            if val == k:
                break
            ops += 1

        return ops


class Solution1:
    """
    leetcode solution
    Runtime 72ms Beats 23.82%
    Memory 17.72MB Beats 53.07%
    """

    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)
