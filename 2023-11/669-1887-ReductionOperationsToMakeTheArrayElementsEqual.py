"""
Leetcode
1887. Reduction Operations to Make the Array Elements Equal (medium)
2023-11-19

Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

    Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
    Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
    Reduce nums[i] to nextLargest.

Return the number of operations to make all elements in nums equal.

 

Example 1:

Input: nums = [5,1,3]
Output: 3
Explanation: It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [3,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [1,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1].

Example 2:

Input: nums = [1,1,1]
Output: 0
Explanation: All elements in nums are already equal.

Example 3:

Input: nums = [1,1,2,2,3]
Output: 4
Explanation: It takes 4 operations to make all elements in nums equal:
1. largest = 3 at index 4. nextLargest = 2. Reduce nums[4] to 2. nums = [1,1,2,2,2].
2. largest = 2 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1,2,2].
3. largest = 2 at index 3. nextLargest = 1. Reduce nums[3] to 1. nums = [1,1,1,1,2].
4. largest = 2 at index 4. nextLargest = 1. Reduce nums[4] to 1. nums = [1,1,1,1,1].

 

Constraints:

    1 <= nums.length <= 5 * 10^4
    1 <= nums[i] <= 5 * 10^4
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums, key=lambda x: -x)
        n = len(nums)
        ans = 0

        def reductions(arr: List[int]) -> int:
            largest = arr[0]
            l = 0
            r = n - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == largest:
                    l = m + 1
                else:
                    r = m - 1

            if l >= len(nums):  # no second largest
                return 0

            ops = l
            nxt_largest = nums[l]
            nums[:l] = [nxt_largest] * ops
            return ops

        while (ops := reductions(nums)) > 0:
            ans += ops

        return ans


class Solution1:
    """
    Runtime: 1629 ms, faster than 5.15% of Python3 online submissions for Reduction Operations to Make the Array Elements Equal.
    Memory Usage: 24.3 MB, less than 39.18% of Python3 online submissions for Reduction Operations to Make the Array Elements Equal.
    """

    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums, key=lambda x: -x)
        n = len(nums)
        largest = nums[0]
        ans = 0

        def reductions(largest_num: int) -> tuple[int, int]:
            largest = largest_num
            l = 0
            r = n - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] >= largest:
                    l = m + 1
                else:
                    r = m - 1

            if l >= len(nums):  # no next largest
                return (0, 0)

            ops = l
            nxt_largest = nums[l]
            return (ops, nxt_largest)

        while True:
            ops, nxt_largest = reductions(largest)
            if ops < 1:
                break
            ans += ops
            largest = nxt_largest

        return ans


class Solution2:
    """
    leetcode solution: Sort and Count
    Runtime: 846 ms, faster than 48.45% of Python3 online submissions for Reduction Operations to Make the Array Elements Equal.
    Memory Usage: 23.8 MB, less than 58.25% of Python3 online submissions for Reduction Operations to Make the Array Elements Equal.
    """

    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        up = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up += 1

            ans += up

        return ans


s = Solution()
tests = [
    ([5, 1, 3],
     3),

    ([1, 1, 1],
     0),

    ([1, 1, 2, 2, 3],
     4)
]
for inp, exp in tests:
    res = s.reductionOperations(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
