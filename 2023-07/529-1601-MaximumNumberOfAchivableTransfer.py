"""
Leetcode
1601. Maximum Number of Achievable Transfer Requests (hard)
2023-07-02

We have n buildings numbered from 0 to n - 1. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array requests where requests[i] = [fromi, toi] represents an employee's request to transfer from building fromi to building toi.

All buildings are full, so a list of requests is achievable only if for each building, the net change in employee transfers is zero. This means the number of employees leaving is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, one employee moving to building 1, and one employee moving to building 2.

Return the maximum number of achievable requests.

Example 1:

Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
Output: 5
Explantion: Let's see the requests:
From building 0 we have employees x and y and both want to move to building 1.
From building 1 we have employees a and b and they want to move to buildings 2 and 0 respectively.
From building 2 we have employee z and they want to move to building 0.
From building 3 we have employee c and they want to move to building 4.
From building 4 we don't have any requests.
We can achieve the requests of users x and b by swapping their places.
We can achieve the requests of users y, a and z by swapping the places in the 3 buildings.

Example 2:

Input: n = 3, requests = [[0,0],[1,2],[2,1]]
Output: 3
Explantion: Let's see the requests:
From building 0 we have employee x and they want to stay in the same building 0.
From building 1 we have employee y and they want to move to building 2.
From building 2 we have employee z and they want to move to building 1.
We can achieve all the requests. 

Example 3:

Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
Output: 4

Constraints:

    1 <= n <= 20
    1 <= requests.length <= 16
    requests[i].length == 2
    0 <= fromi, toi < n
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def requests_possible(self, n: int, reqs: List[List[int]]):
        buildings = [0] * n
        for a, b in reqs:
            buildings[a] -= 1
            buildings[b] += 1
        return all(x == 0 for x in buildings)

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        q = [requests]
        while q:
            reqs = q.pop(0)
            if self.requests_possible(n, reqs):
                return len(reqs)
            q += list(reqs[:i] + reqs[i+1:] for i in range(len(reqs)))
        return 0


class Solution1:
    """
    leetcode solution 1: backtracking
    N = number of buildings, M = number of requests
    Time: O(2^M * N)
    Space: O(N + M)
    Runtime: 1495 ms, faster than 48.54% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
    Memory Usage: 16.3 MB, less than 95.15% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
    """
    ans = 0

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.ans = 0
        indegree = [0] * n
        self.maxReq(requests, indegree, n, 0, 0)
        return self.ans

    def maxReq(self, reqs: List[List[int]], indegree: List[int], n: int, index: int, count: int):
        if index == len(reqs):
            # check if all buildings have an in-degree of 0
            if all(i == 0 for i in indegree):
                self.ans = max(self.ans, count)
            return

        # consider this request, increment and decrement for the buildings involved
        a, b = reqs[index]
        indegree[a] -= 1
        indegree[b] += 1

        # move to the next request and also increment the count of requests
        self.maxReq(reqs, indegree, n, index + 1, count + 1)

        # backtrack to the previous values to move back to the origial state
        # before the second recursion
        indegree[a] += 1
        indegree[b] -= 1

        # ignore this request and move on to the next request without
        # incrementing the count
        self.maxReq(reqs, indegree, n, index + 1, count)


class Solution2:
    """
    leetcode solution 2: bitmasking
    https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/solution/1952937
    Runtime: 2290 ms, faster than 28.15% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
    Memory Usage: 16.4 MB, less than 81.55% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
    """

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        m = len(requests)

        for i in range(2**m):
            indegree = [0] * n
            bit_count = i.bit_count()
            if bit_count > ans:
                j = 2**(m - 1)
                for k in range(m):
                    if i & j:
                        a, b = requests[k]
                        indegree[a] -= 1
                        indegree[b] += 1
                    j = j >> 1
                if all(x == 0 for x in indegree):
                    ans = bit_count

        return ans


s = Solution1()
tests = [
    ((5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]),
     5),

    ((3, [[0, 0], [1, 2], [2, 1]]),
     3),

    ((4, [[0, 3], [3, 1], [1, 2], [2, 0]]),
     4),
]
for inp, exp in tests:
    res = s.maximumRequests(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
