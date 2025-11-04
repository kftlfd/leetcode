"""
Leetcode
2025-11-04
3318. Find X-Sum of All K-Long Subarrays I
Easy

You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

    Count the occurrences of all elements in the array.
    Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
    Calculate the sum of the resulting array.

Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the

nums[i..i + k - 1].

 

Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

    For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
    For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
    For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.

Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

 

Constraints:

    1 <= n == nums.length <= 50
    1 <= nums[i] <= 50
    1 <= x <= k <= nums.length


Hint 1
Implement the x-sum function. Then, run x-sum on every subarray of nums of size k.
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime 23ms Beats 74.81%
    Memory 17.73MB Beats 83.64%
    """

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        return [self.get_x_sum(nums[i-k:i], x) for i in range(k, len(nums) + 1)]

    def get_x_sum(self, nums: List[int], x: int) -> int:
        cnt = Counter(sorted(nums, reverse=True))
        return sum(num * freq for num, freq in cnt.most_common(x))


class Solution1:
    """
    leetcode solution: Hash Table + Sorting
    Runtime 31ms Beats 33.77%
    Memory 17.78MB Beats 83.64%
    """

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = list()
        for i in range(n - k + 1):
            cnt = Counter(nums[i: i + k])
            freq = sorted(cnt.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum(key * value for key, value in freq[:x])
            ans.append(xsum)
        return ans
