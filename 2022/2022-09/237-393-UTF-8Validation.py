"""
Leetcode
393. UTF-8 Validation (medium)
2022-09-13

Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

 1. For a 1-byte character, the first bit is a 0, followed by its Unicode code.
 2. For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

x denotes a bit in the binary form of a byte that may be either 0 or 1.

Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:
Input: data = [197,130,1]
Output: true
Explanation: data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:
Input: data = [235,140,4]
Output: false
Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
"""

from typing import List


# Runtime: 154 ms, faster than 71.93% of Python3 online submissions for UTF-8 Validation.
# Memory Usage: 14.2 MB, less than 70.76% of Python3 online submissions for UTF-8 Validation.
class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        i = 0
        while i < len(data):

            char = format(data[i], '08b')

            idx = 0
            try:
                idx = char.index("0")
            except:
                return False

            if idx == 0:
                i += 1
                continue

            if idx == 1 or idx > 4:
                return False

            to_check = data[i+1: i+idx]

            if len(to_check) != idx-1:
                return False

            if not all([format(x, '08b')[:2] == '10' for x in to_check]):
                return False

            i += idx

        return True


# leetcode solution - Approach 2: Bit Manipulation
# Runtime: 105 ms, faster than 99.56% of Python3 online submissions for UTF-8 Validation.
# Memory Usage: 14.2 MB, less than 35.67% of Python3 online submissions for UTF-8 Validation.
class Solution1:
    def validUtf8(self, data: List[int]) -> bool:
        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # Mask to check if the most significant bit (8th bit from the left) is set or not
        mask1 = 1 << 7

        # Mask to check if the second most significant bit is set or not
        mask2 = 1 << 6
        for num in data:

            # Get the number of set most significant bits in the byte if
            # this is the starting byte of an UTF-8 character.
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1

                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:

                # If this byte is a part of an existing UTF-8 character, then we
                # simply have to look at the two most significant bits and we make
                # use of the masks we defined before.
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_bytes -= 1
        return n_bytes == 0


s = Solution()
tests = [
    [237],
    [197, 130, 1],
    [235, 140, 4],
]
for t in tests:
    print(t)
    print(s.validUtf8(t))
    print()
