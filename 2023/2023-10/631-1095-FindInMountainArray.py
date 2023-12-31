"""
Leetcode
1095. Find in Mountain Array (hard)
2023-10-12

(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

    MountainArray.get(k) returns the element of the array at index k (0-indexed).
    MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

 

Constraints:

    3 <= mountain_arr.length() <= 10^4
    0 <= target <= 10^9
    0 <= mountain_arr.get(index) <= 10^9
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """

# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class MountainArray:
    def __init__(self, arr: list) -> None:
        self.arr = arr

    def get(self, index: int):
        return self.arr[index]

    def length(self):
        return len(self.arr)


class Solution:
    """
    leetcode solution 1: binary search
    Time: O(log(n))
    Space: O(1)
    Runtime: 41 ms, faster than 41.71% of Python3 online submissions for Find in Mountain Array.
    Memory Usage: 17 MB, less than 98.91% of Python3 online submissions for Find in Mountain Array.
    """

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        arr = mountain_arr
        length = arr.length()

        # 1. find index of peak
        low = 1
        high = length - 2
        while low != high:
            m = low + (high - low) // 2
            if arr.get(m) < arr.get(m + 1):
                low = m + 1
            else:
                high = m
        peak_index = low

        # 2. search in left part (increasing)
        low = 0
        high = peak_index
        while low != high:
            m = low + (high - low) // 2
            if arr.get(m) < target:
                low = m + 1
            else:
                high = m
        if arr.get(low) == target:
            return low

        # 3. search in right part (decreasing)
        low = peak_index + 1
        high = length - 1
        while low != high:
            m = low + (high - low) // 2
            if arr.get(m) > target:
                low = m + 1
            else:
                high = m
        if arr.get(low) == target:
            return low

        return -1


class Solution1:
    """
    leetcode solution 2: Minimizing get Calls with Early Stopping and Caching
    Time: O(log(n))
    Space: O(log(n))
    Runtime: 29 ms, faster than 96.74% of Python3 online submissions for Find in Mountain Array.
    Memory Usage: 17.2 MB, less than 60.00% of Python3 online submissions for Find in Mountain Array.
    """

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Save the length of the mountain array
        length = mountain_arr.length()

        # Initialize the cache
        cache = {}

        # 1. Find the index of the peak element
        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) >> 1

            if test_index in cache:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)
                cache[test_index] = curr

            if test_index + 1 in cache:
                next = cache[test_index + 1]
            else:
                next = mountain_arr.get(test_index + 1)
                cache[test_index + 1] = next

            if curr < next:
                if curr == target:
                    return test_index
                if next == target:
                    return test_index + 1
                low = test_index + 1
            else:
                high = test_index

        peak_index = low

        # 2. Search in the strictly increasing part of the array
        # If found, will be returned in the loop itself.
        low = 0
        high = peak_index
        while low <= high:
            test_index = (low + high) >> 1

            if test_index in cache:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)

            if curr == target:
                return test_index
            elif curr < target:
                low = test_index + 1
            else:
                high = test_index - 1

        # 3. Search in the strictly decreasing part of the array
        # If found, will be returned in the loop itself.
        low = peak_index + 1
        high = length - 1
        while low <= high:
            test_index = (low + high) >> 1

            if test_index in cache:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)

            if curr == target:
                return test_index
            elif curr > target:
                low = test_index + 1
            else:
                high = test_index - 1

        # Target is not present in the mountain array
        return -1
