"""
Leetcode
2026-10-22
3942. Minimum Operations to Sort a Permutation
Medium

You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.

You may perform only the following operations:

    Reverse the entire array.
    Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.

Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

 

Example 1:

Input: nums = [0,2,1]

Output: 2

Explanation:

    Rotate Left by one: [2, 1, 0]
    Reverse the array: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal

Example 2:

Input: nums = [1,0,2]

Output: 2

Explanation:

    Reverse the array: [2, 0, 1]
    Rotate Left by one: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal.

Example 3:

Input: nums = [2,0,1,3]

Output: -1

Explanation:

It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.

 

Constraints:

    1 <= n == nums.length <= 10^5
    0 <= nums[i] <= n - 1
    nums is a permutation of integers from 0 to n - 1.


Hint 1
1a. (Case Analysis) The operations generate only rotations of nums and rotations of reverse(nums).
Hint 2
1b. (Case Analysis) So sorting is possible if and only if nums is a rotation of increasing order, or a rotation of decreasing order.
Hint 3
1c. (Case Analysis) If nums is increasing cyclically and nums[i] = 0, then rotating left i times sorts the array, or we may reverse, rotate, then reverse again. Take the minimum between these possibilities.
Hint 4
1d. (Case Analysis) If nums is decreasing cyclically, try both possibilities: reverse first, or rotate first and then reverse. Take the minimum valid cost.
Hint 5
2a. (Breadth-First Search) As follows from Hint 1a and 1b, each reachable array can be represented as a state. Since all reachable arrays belong to one of two families, we can compress a state into (type, shift). type = 0: a rotation of the original array. type = 1: a rotation of the reversed array. shift denotes the number of left rotations applied within that family.
Hint 6
2b. (Breadth-First Search) A left rotation changes shift to (shift + 1) % n. A reverse toggles type, while also changing the corresponding shift to (n - shift) % n.
Hint 7
2c. (Breadth-First Search) Build a graph on these 2n states using the two allowed operations, then run BFS from (0, 0) to the state representing the input array.
"""

from typing import List


class Solution1:
    """
    leetcode solution: Simulation
    Runtime 71ms Beats 71.91%
    Memory 31.33MB Beats 86.52%
    """

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        start = nums.index(0)

        asc = True
        desc = True

        for i in range(1, n):
            value = nums[(start + i) % n]

            if value != i:
                asc = False
            if value != n - i:
                desc = False

            if not asc and not desc:
                return -1

        if asc:
            return min(start, n - start + 2)

        return min(n - start, start + 2)
