"""
Leetcode
2024-12-01
1346. Check If N and Its Double Exist
Easy

Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.

 

Constraints:

    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3

Hints:
- Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].
- On each step of the loop check if we have seen the element 2 * arr[i] so far.
- Also check if we have seen arr[i] / 2 in case arr[i] % 2 == 0.
"""

from typing import List


class Solution01:
    """
    Runtime: 4 ms, faster than 42.81% of Python3 online submissions for Check If N and Its Double Exist.
    Memory Usage: 17.3 MB, less than 5.25% of Python3 online submissions for Check If N and Its Double Exist.
    """

    def checkIfExist(self, arr: List[int]) -> bool:
        nums = sorted(arr)
        n = len(nums)

        def find(val: int):
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2
                cur = nums[mid]
                if cur == val:
                    return mid
                if cur > val:
                    right = mid
                else:
                    left = mid + 1

            return -1

        for i, num in enumerate(nums):
            j = find(num * 2)
            if j >= 0 and j != i:
                return True

        return False


class Solution02:
    """
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Check If N and Its Double Exist.
    Memory Usage: 17.3 MB, less than 5.25% of Python3 online submissions for Check If N and Its Double Exist.
    """

    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set()

        for num in arr:
            if num * 2 in nums or (num % 2 == 0 and num // 2 in nums):
                return True
            nums.add(num)

        return False
