"""
Leetcode
1282. Group the People Given the Group Size They Belong To (medium)
2023-09-11

There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

Constraints:

    groupSizes.length == n
    1 <= n <= 500
    1 <= groupSizes[i] <= n
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    Runtime: 69 ms, faster than 84.71% of Python3 online submissions for Group the People Given the Group Size They Belong To.
    Memory Usage: 16.3 MB, less than 91.52% of Python3 online submissions for Group the People Given the Group Size They Belong To.
    """

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        ht = defaultdict(list)

        for person, group_size in enumerate(groupSizes):
            ht[group_size].append(person)

        ans = []

        for group_size, people in ht.items():
            for i in range(0, len(people), group_size):
                ans.append(people[i:i+group_size])

        return ans


class Solution1:
    """
    https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/solution/2052714
    Runtime: 71 ms, faster than 79.24% of Python3 online submissions for Group the People Given the Group Size They Belong To.
    Memory Usage: 16.5 MB, less than 31.58% of Python3 online submissions for Group the People Given the Group Size They Belong To.
    """

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        res = []
        for pid, group_size in enumerate(groupSizes):
            groups[group_size].append(pid)
            if len(groups[group_size]) == group_size:
                res.append(groups.pop(group_size))
        return res
