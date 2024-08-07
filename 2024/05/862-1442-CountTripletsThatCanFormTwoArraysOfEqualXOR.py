"""
Leetcode
1442. Count Triplets That Can Form Two Arrays of Equal XOR
Medium
2024-05-30

Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

    a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
    b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:

Input: arr = [1,1,1,1,1]
Output: 10

 

Constraints:

    1 <= arr.length <= 300
    1 <= arr[i] <= 10^8


Hints:
- We are searching for sub-array of length ≥ 2 and we need to split it to 2 non-empty arrays so that the xor of the first array is equal to the xor of the second array. This is equivalent to searching for sub-array with xor = 0.
- Keep the prefix xor of arr in another array, check the xor of all sub-arrays in O(n^2), if the xor of sub-array of length x is 0 add x-1 to the answer.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    leetcode solution 4: One Pass Prefix XOR
    Runtime: 40 ms, faster than 87.36% of Python3 online submissions for Count Triplets That Can Form Two Arrays of Equal XOR.
    Memory Usage: 16.6 MB, less than 26.44% of Python3 online submissions for Count Triplets That Can Form Two Arrays of Equal XOR.
    """

    def countTriplets(self, arr: List[int]) -> int:
        size = len(arr)
        count = 0
        prefix = 0

        # Dictionaries to store counts and totals of XOR values encountered
        count_map = defaultdict(int)
        count_map[0] = 1
        total_map = defaultdict(int)

        # Iterating through the array
        for i in range(size):
            # Calculating XOR prefix
            prefix ^= arr[i]

            # Calculating contribution of current element to the result
            count += count_map[prefix] * i - total_map[prefix]

            # Updating total count of current XOR value
            total_map[prefix] += i + 1
            count_map[prefix] += 1

        return count
