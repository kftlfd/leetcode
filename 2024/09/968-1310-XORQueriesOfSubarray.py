"""
Leetcode
2024-09-13
1310. XOR Queries of a Subarray
Medium

You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.

 

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8

Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]

 

Constraints:

    1 <= arr.length, queries.length <= 3 * 10^4
    1 <= arr[i] <= 10^9
    queries[i].length == 2
    0 <= lefti <= righti < arr.length
"""

from typing import List


class Solution:
    """
    Runtime: 306 ms, faster than 49.06% of Python3 online submissions for XOR Queries of a Subarray.
    Memory Usage: 31.5 MB, less than 10.11% of Python3 online submissions for XOR Queries of a Subarray.
    """

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0] * (len(arr) + 1)
        xors[1] = arr[0]
        for i in range(2, len(arr) + 1):
            xors[i] = arr[i-1] ^ xors[i-1]

        out = [0] * len(queries)

        for i, (left, right) in enumerate(queries):
            if left == 0:
                out[i] = xors[right+1]
            else:
                out[i] = xors[right+1] ^ xors[left]

        return out


class Solution2:
    """
    leetcode solution 2: Prefix XOR Array
    Runtime: 301 ms, faster than 67.04% of Python3 online submissions for XOR Queries of a Subarray.
    Memory Usage: 31.3 MB, less than 34.46% of Python3 online submissions for XOR Queries of a Subarray.
    """

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Build prefix XOR array
        prefix_xor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        # Store the XOR result for each query in a variable
        result = [prefix_xor[r + 1] ^ prefix_xor[l] for l, r in queries]
        return result
