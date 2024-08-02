"""
Leetcode
2134. Minimum Swaps to Group All 1's Together II
Medium
2024-08-02

A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

 

Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.

Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.

Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.

 

Constraints:

    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.

Hints:
- Notice that the number of 1’s to be grouped together is fixed. It is the number of 1's the whole array has.
- Call this number total. We should then check for every subarray of size total (possibly wrapped around), how many swaps are required to have the subarray be all 1’s.
- The number of swaps required is the number of 0’s in the subarray.
- To eliminate the circular property of the array, we can append the original array to itself. Then, we check each subarray of length total.
- How do we avoid recounting the number of 0’s in the subarray each time? The Sliding Window technique can help.    
"""

from typing import List


class Solution:
    """
    Runtime: 667 ms, faster than 85.13% of Python3 online submissions for Minimum Swaps to Group All 1's Together II.
    Memory Usage: 20.7 MB, less than 37.84% of Python3 online submissions for Minimum Swaps to Group All 1's Together II.
    """

    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones_n = sum(nums)
        window_sum = sum(nums[:ones_n])
        ans = ones_n - window_sum

        for i in range(ones_n, n + ones_n):
            window_sum += nums[i % n]
            window_sum -= nums[i - ones_n]
            ans = min(ans, ones_n - window_sum)

        return ans


s = Solution()
tests = [
    ([0, 1, 0, 1, 1, 0, 0],
     1),

    ([0, 1, 1, 1, 0, 0, 1, 1, 0],
     2),

    ([1, 1, 0, 0, 1],
     0),
]
for inp, exp in tests:
    res = s.minSwaps(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
