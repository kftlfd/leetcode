"""
Leetcode
1575. Count All Possible Routes (hard)
2023-06-25

You are given an array of distinct positive integers locations where locations[i] represents the position of city i. You are also given integers start, finish and fuel representing the starting city, ending city, and the initial amount of fuel you have, respectively.

At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value of x.

Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more than once (including start and finish).

Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
Output: 4
Explanation: The following are all possible routes, each uses 5 units of fuel:
1 -> 3
1 -> 2 -> 3
1 -> 4 -> 3
1 -> 4 -> 2 -> 3

Example 2:

Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
Output: 5
Explanation: The following are all possible routes:
1 -> 0, used fuel = 1
1 -> 2 -> 0, used fuel = 5
1 -> 2 -> 1 -> 0, used fuel = 5
1 -> 0 -> 1 -> 0, used fuel = 3
1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5

Example 3:

Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
Output: 0
Explanation: It is impossible to get from 0 to 2 using only 3 units of fuel since the shortest route needs 4 units of fuel.

Constraints:

    2 <= locations.length <= 100
    1 <= locations[i] <= 10^9
    All integers in locations are distinct.
    0 <= start, finish < locations.length
    1 <= fuel <= 200
"""

from typing import List


class Solution:
    """
    leetcode solution 1: recursive DP
    Time: O(n^2 * m) -- m = fuel
    Space: O(n * m)
    Runtime: 2981 ms, faster than 25.56% of Python3 online submissions for Count All Possible Routes.
    Memory Usage: 22.7 MB, less than 56.39% of Python3 online submissions for Count All Possible Routes.
    """

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10**9 + 7
        memo = {}

        def solve(curr_city, remaining_fuel):
            if remaining_fuel < 0:
                return 0

            if (curr_city, remaining_fuel) in memo:
                return memo[(curr_city, remaining_fuel)]

            ans = 1 if curr_city == finish else 0

            for next_city in range(n):
                if next_city != curr_city:
                    ans = (ans + solve(next_city, remaining_fuel - abs(
                        locations[curr_city] - locations[next_city]
                    ))) % mod

            memo[(curr_city, remaining_fuel)] = ans
            return ans

        return solve(start, fuel)


class Solution1:
    """
    leetcode solution 2: iterative DP
    Time: O(n^2 * m) -- m = fuel
    Space: O(n * m)
    Runtime: 8572 ms, faster than 5.26% of Python3 online submissions for Count All Possible Routes.
    Memory Usage: 17.2 MB, less than 91.73% of Python3 online submissions for Count All Possible Routes.
    """

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10**9 + 7
        dp = [[0] * (fuel + 1) for _ in range(n)]

        for i in range(fuel + 1):
            dp[finish][i] = 1

        for j in range(fuel + 1):
            for i in range(n):
                for k in range(n):
                    if k == i:
                        continue
                    if abs(locations[i] - locations[k]) <= j:
                        dp[i][j] = (
                            dp[i][j] + dp[k][j - abs(locations[i] - locations[k])]) % mod

        return dp[start][fuel]


s = Solution1()
tests = [
    (([2, 3, 6, 8, 4], 1, 3, 5),
     4),

    (([4, 3, 1], 1, 0, 6),
     5),

    (([5, 2, 1], 0, 2, 3),
     0),
]
for inp, exp in tests:
    res = s.countRoutes(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
