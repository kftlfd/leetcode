"""
Leetcode
1356. Sort Integers by The Number of 1 Bits (easy)
2023-10-30

You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

 

Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.

 

Constraints:

    1 <= arr.length <= 500
    0 <= arr[i] <= 10^4
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    Runtime: 69 ms, faster than 57.56% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    Memory Usage: 16.2 MB, less than 94.41% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    """

    def sortByBits(self, arr: List[int]) -> List[int]:

        by_bits = defaultdict(list)

        for num in arr:
            by_bits[bin(num).count("1")].append(num)

        ans = []

        for _, bit_group in sorted(by_bits.items()):
            ans += sorted(bit_group)

        return ans


class Solution1:
    """
    leetcode solution 1: Sort By Custom Comparator: Built-in
    Time: O(n * log(n))
    Space: O(n)
    Runtime: 60 ms, faster than 89.93% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    Memory Usage: 16.4 MB, less than 75.72% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    """

    def sortByBits(self, arr: List[int]) -> List[int]:

        return sorted(arr, key=lambda num: (num.bit_count(), num))


class Solution2:
    """
    leetcode solution 2: Bit Manipulation
    Time: O(n * log(n))
    Space: O(n)
    Runtime: 74 ms, faster than 37.72% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    Memory Usage: 16.4 MB, less than 75.72% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    """

    def sortByBits(self, arr: List[int]) -> List[int]:

        def find_weight(num):
            mask = 1
            weight = 0

            while num:
                if num & mask:
                    weight += 1
                    num ^= mask

                mask <<= 1

            return weight

        arr.sort(key=lambda num: (find_weight(num), num))
        return arr


class Solution3:
    """
    leetcode solution 3: Brian Kerninghan's Algorithm
    Time: O(n * log(n))
    Space: O(n)
    Runtime: 71 ms, faster than 48.94% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    Memory Usage: 16.5 MB, less than 47.11% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    """

    def sortByBits(self, arr: List[int]) -> List[int]:

        def find_weight(num):
            weight = 0

            while num:
                weight += 1
                num &= (num - 1)

            return weight

        arr.sort(key=lambda num: (find_weight(num), num))
        return arr
