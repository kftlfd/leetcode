"""
Leetcode
1481. Least Number of Unique Integers after K Removals
Medium
2024-02-16

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:

Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

 

Constraints:

    1 <= arr.length <= 10^5
    1 <= arr[i] <= 10^9
    0 <= k <= arr.length
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 355 ms, faster than 57.69% of Python3 online submissions for Least Number of Unique Integers after K Removals.
    Memory Usage: 33.6 MB, less than 75.53% of Python3 online submissions for Least Number of Unique Integers after K Removals.
    """

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        removals_left = k

        for num, count in reversed(list(cnt.most_common())):
            if removals_left >= count:
                del cnt[num]
                removals_left -= count
            else:
                break

        return len(cnt)


class Solution3:
    """
    leetcode solution 3: counting sort
    Runtime: 335 ms, faster than 72.07% of Python3 online submissions for Least Number of Unique Integers after K Removals.
    Memory Usage: 32.5 MB, less than 99.80% of Python3 online submissions for Least Number of Unique Integers after K Removals.
    """

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Dictionary to track the frequencies of elements
        hmap = {}
        for i in arr:
            hmap[i] = hmap.get(i, 0) + 1

        n = len(arr)

        # List to track the frequencies of frequencies
        # The maximum possible frequency of any element
        # will be n, so we'll initialize this list with size n + 1
        count_of_frequencies = [0] * (n + 1)

        # Populating count_of_frequencies list
        for count in hmap.values():
            count_of_frequencies[count] += 1

        # Variable to track the remaining number of unique elements
        remaining_unique_elements = len(hmap)

        # Traversing over all possible frequencies
        for i in range(1, n + 1):
            # For each possible frequency i, we'd like to remove as
            # many elements with that frequency as possible.
            # k // i represents the number of maximum possible elements
            # we could remove with k elements left to remove.
            # count_of_frequencies[i] represents the actual number of elements
            # with frequency i.
            num_elements_to_remove = min(k // i, count_of_frequencies[i])

            # Removing the maximum possible elements
            k -= (i * num_elements_to_remove)

            # num_elements_to_remove is the count of unique elements removed
            remaining_unique_elements -= num_elements_to_remove

            # If the number of elements that can be removed is less
            # than the current frequency, we won't be able to remove
            # any more elements with a higher frequency so we can return
            # the remaining number of unique elements
            if k < i:
                return remaining_unique_elements

        # We have traversed all possible frequencies i.e.,
        # removed all elements. Returning 0 in this case.
        return 0
