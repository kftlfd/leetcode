"""
Leetcode
2149. Rearrange Array Elements by Sign
Medium
2024-02-14

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].

 

Constraints:

    2 <= nums.length <= 2 * 105
    nums.length is even
    1 <= |nums[i]| <= 105
    nums consists of equal number of positive and negative integers.
"""

from typing import List


class Solution:
    """
    Runtime: 1037 ms, faster than 42.09% of Python3 online submissions for Rearrange Array Elements by Sign.
    Memory Usage: 47.2 MB, less than 74.45% of Python3 online submissions for Rearrange Array Elements by Sign.
    """

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        ans = []
        for p, n in zip(pos, neg):
            ans.append(p)
            ans.append(n)

        return ans


class Solution1:
    """
    leetcode solution: Two Pointers
    Runtime: 984 ms, faster than 96.01% of Python3 online submissions for Rearrange Array Elements by Sign.
    Memory Usage: 47.3 MB, less than 65.62% of Python3 online submissions for Rearrange Array Elements by Sign.
    """

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos_idx = 0
        neg_idx = 1

        for num in nums:
            if num > 0:
                ans[pos_idx] = num
                pos_idx += 2
            else:
                ans[neg_idx] = num
                neg_idx += 2

        return ans
