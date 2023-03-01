"""
Leetcode
912. Sort an Array (medium)
2023-03-01

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
"""

from typing import List


class Solution:
    """
    merge sort
    Runtime: 2396 ms, faster than 25.49% of Python3 online submissions for Sort an Array.
    Memory Usage: 23.3 MB, less than 26.39% of Python3 online submissions for Sort an Array.
    """

    def sortArray(self, nums: List[int]) -> List[int]:

        l = len(nums)

        if l == 1:
            return nums

        sorted_left = self.sortArray(nums[:l//2])

        sorted_right = self.sortArray(nums[l//2:])

        arr = []

        while sorted_left and sorted_right:
            if sorted_left[0] < sorted_right[0]:
                arr.append(sorted_left.pop(0))
            else:
                arr.append(sorted_right.pop(0))

        if sorted_left:
            arr += sorted_left
        elif sorted_right:
            arr += sorted_right

        return arr


class Solution1:
    """
    leetcode solution 3: counting sort
    Runtime: 806 ms, faster than 86.90% of Python3 online submissions for Sort an Array.
    Memory Usage: 27.2 MB, less than 13.47% of Python3 online submissions for Sort an Array.
    """

    def sortArray(self, nums: List[int]) -> List[int]:

        counts = {}

        min_val, max_val = min(nums), max(nums)

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        index = 0
        for val in range(min_val, max_val + 1):
            while counts.get(val, 0) > 0:
                nums[index] = val
                counts[val] -= 1
                index += 1

        return nums


class Solution2:
    """
    leetcode solution 4: Radix Sort
    Runtime: 1254 ms, faster than 82.12% of Python3 online submissions for Sort an Array.
    Memory Usage: 22.7 MB, less than 42.11% of Python3 online submissions for Sort an Array.
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        # Find the absolute maximum element to find max number of digits.
        max_element = nums[0]
        for val in nums:
            max_element = max(abs(val), max_element)

        max_digits = 0
        while max_element > 0:
            max_digits += 1
            max_element = max_element // 10

        place_value = 1

        # Bucket sort function for each place value digit.
        def bucket_sort():
            buckets = [[] for i in range(10)]
            # Store the respective number based on it's digit.
            for val in nums:
                digit = abs(val) / place_value
                digit = int(digit % 10)
                buckets[digit].append(val)

            # Overwrite 'nums' in sorted order of current place digits.
            index = 0
            for digit in range(10):
                for val in buckets[digit]:
                    nums[index] = val
                    index += 1

        # Radix sort, least significant digit place to most significant.
        for _ in range(max_digits):
            bucket_sort()
            place_value *= 10

        # Seperate out negatives and reverse them.
        positives = [val for val in nums if val >= 0]
        negatives = [val for val in nums if val < 0]
        negatives.reverse()

        # Final 'arr' will be 'negative' elements, then 'positive' elements.
        return negatives + positives


class Solution3:
    """
    python built-in
    Runtime: 679 ms, faster than 93.53% of Python3 online submissions for Sort an Array.
    Memory Usage: 22 MB, less than 68.37% of Python3 online submissions for Sort an Array.
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)


s = Solution()
tests = [
    [5, 2, 3, 1],
    [5, 1, 1, 2, 0, 0],
]
for inp in tests:
    exp = sorted(inp)
    res = s.sortArray(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
