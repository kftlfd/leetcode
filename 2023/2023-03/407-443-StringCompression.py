"""
Leetcode
443. String Compression (medium)
2023-03-02

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""

from typing import List


class Solution:
    """
    Runtime: 65 ms, faster than 45.31% of Python3 online submissions for String Compression.
    Memory Usage: 14 MB, less than 65.01% of Python3 online submissions for String Compression.
    """

    def compress(self, chars: List[str]) -> int:

        out = []

        i = 0
        while i < len(chars):

            out.append(chars[i])

            group_len = 1
            while i + 1 < len(chars) and chars[i + 1] == chars[i]:
                group_len += 1
                i += 1

            if group_len > 1:
                out += list(str(group_len))

            i += 1

        chars[:] = out
        return len(out)


class Solution1:
    """
    leetcode solution
    Runtime: 60 ms, faster than 73.48% of Python3 online submissions for String Compression.
    Memory Usage: 13.9 MB, less than 65.01% of Python3 online submissions for String Compression.
    """

    def compress(self, chars: List[str]) -> int:

        i = 0
        char = 0
        while i < len(chars):

            group_len = 1
            while i + group_len < len(chars) and chars[i + group_len] == chars[i]:
                group_len += 1

            chars[char] = chars[i]
            char += 1

            if group_len > 1:
                group_repr = list(str(group_len))
                chars[char:char + len(group_repr)] = group_repr
                char += len(group_repr)

            i += group_len

        return char


s = Solution1()
tests = [
    (["a", "a", "a", "b", "b", "a", "a"],
     (6, ["a", "3", "b", "2", "a", "2"])),

    (["a", "a", "b", "b", "c", "c", "c"],
     (6, ["a", "2", "b", "2", "c", "3"])),

    (["a"],
     (1, ["a"])),

    (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
     (4, ["a", "b", "1", "2"]))
]
for inp, exp in tests:
    exp_val, exp_compressed = exp
    to_compress = inp[:]
    res = s.compress(to_compress)
    if (res, to_compress[:exp_val]) != (exp_val, exp_compressed):
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', (res, to_compress))
        print()
print('Completed testing')
