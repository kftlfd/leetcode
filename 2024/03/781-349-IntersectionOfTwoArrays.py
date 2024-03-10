"""
Leetcode
349. Intersection of Two Arrays
Easy
2024-03-10

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

 

Constraints:

    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000
"""

from typing import List


class Solution:
    """
    Runtime: 47 ms, faster than 65.21% of Python3 online submissions for Intersection of Two Arrays.
    Memory Usage: 16.7 MB, less than 91.42% of Python3 online submissions for Intersection of Two Arrays.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


class Solution1:
    """
    leetcode solution 1: Sorting and Two Pointers
    Runtime: 45 ms, faster than 74.57% of Python3 online submissions for Intersection of Two Arrays.
    Memory Usage: 16.8 MB, less than 53.45% of Python3 online submissions for Intersection of Two Arrays.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Sort both arrays
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        # Initialize two pointers
        N = len(nums1)
        M = len(nums2)
        p1 = 0
        p2 = 0

        # Create set that stores integers appearing in both arrays
        intersection = set()

        while p1 < N and p2 < M:
            # Add a value to the set if values at both pointers equal
            if nums1[p1] == nums2[p2]:
                intersection.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        # Convert intersection to an array
        result = []
        for x in intersection:
            result.append(x)

        # Return the result
        return result


class Solution2:
    """
    leetcode solution 2: Built-in Set Intersection
    Runtime: 36 ms, faster than 98.33% of Python3 online submissions for Intersection of Two Arrays.
    Memory Usage: 16.8 MB, less than 53.45% of Python3 online submissions for Intersection of Two Arrays.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)


class Solution3:
    """
    leetcode solution 3: Two Sets
    Runtime: 53 ms, faster than 33.80% of Python3 online submissions for Intersection of Two Arrays.
    Memory Usage: 16.7 MB, less than 91.42% of Python3 online submissions for Intersection of Two Arrays.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)

    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]


class Solution4:
    """
    leetcode solution 4: One Dictionary
    Runtime: 56 ms, faster than 23.33% of Python3 online submissions for Intersection of Two Arrays.
    Memory Usage: 16.8 MB, less than 53.45% of Python3 online submissions for Intersection of Two Arrays.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize seen dictionary and res array
        seen = {}
        result = []

        # mark values occurring in nums1
        for x in nums1:
            seen[x] = 1

        for x in nums2:
            # Check if x is in the dictionary and not in the result
            if x in seen and seen[x] == 1:
                result.append(x)
                seen[x] = 0

        # Return the result
        return result
