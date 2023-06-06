"""
Leetcode
1502. Can Make Arithmetic Progression From Sequence (easy)
2023-06-06

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:

    2 <= arr.length <= 1000
    -106 <= arr[i] <= 106
"""

from typing import List


class Solution:
    """
    Runtime: 54 ms, faster than 43.48% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
    Memory Usage: 16.6 MB, less than 20.83% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
    """

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        nums = sorted(arr)
        diff = nums[1] - nums[0]

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] != diff:
                return False

        return True


class Solution1:
    """
    leetcode solution 2: Set
    Runtime: 57 ms, faster than 32.76% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
    Memory Usage: 16.4 MB, less than 51.64% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
    """

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_val, max_val = min(arr), max(arr)
        n = len(arr)

        if max_val - min_val == 0:
            return True

        if (max_val - min_val) % (n - 1):
            return False

        diff = (max_val - min_val) // (n - 1)
        nums = set()

        for a in arr:
            if (a - min_val) % diff:
                return False
            nums.add(a)

        return len(nums) == n


class Solution2:
    """
    leetcode solution 3: In-place Modification
    Runtime: 57 ms, faster than 32.76% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
    Memory Usage: 16.5 MB, less than 20.83% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
    """

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_val, max_val = min(arr), max(arr)
        n = len(arr)

        if (max_val - min_val) % (n - 1) != 0:
            return False

        diff = (max_val - min_val) // (n - 1)
        i = 0

        while i < n:
            # if arr[i] is at the correct index, move on
            if arr[i] == min_val + i * diff:
                i += 1

            # if arr[i] doesn't belong to this arithmetic sequence, return False
            elif (arr[i] - min_val) % diff != 0:
                return False

            # otherwise, find the index j to which arr[i] belongs, swap arr[j] with arr[i]
            else:
                j = (arr[i] - min_val) // diff

                # if we find duplicated elements, return False
                if arr[i] == arr[j]:
                    return False

                # swap arr[i] with arr[j]
                arr[i], arr[j] = arr[j], arr[i]

        return True


s = Solution2()
tests = [
    ([3, 5, 1],
     True),

    ([1, 2, 4],
     False),
]
for inp, exp in tests:
    res = s.canMakeArithmeticProgression(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
