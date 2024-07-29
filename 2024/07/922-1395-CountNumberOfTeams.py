"""
Leetcode
1395. Count Number of Teams
Medium
2024-07-29

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

    Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
    A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:

Input: rating = [1,2,3,4]
Output: 4

 

Constraints:

    n == rating.length
    3 <= n <= 1000
    1 <= rating[i] <= 10^5
    All the integers in rating are unique.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    v1, v2, v3 = rating[i], rating[j], rating[k]
                    if v1 < v2 < v3 or v1 > v2 > v3:
                        ans += 1

        return ans


class Solution1:
    """
    leetcode solution 1: Dynamic Programming (Memoization)
    Runtime: 1695 ms, faster than 5.04% of Python3 online submissions for Count Number of Teams.
    Memory Usage: 17 MB, less than 12.33% of Python3 online submissions for Count Number of Teams.
    """

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        increasing_cache = [[-1] * 4 for _ in range(n)]
        decreasing_cache = [[-1] * 4 for _ in range(n)]

        # Calculate total teams by considering each soldier as a starting point
        for start_index in range(n):
            teams += self._count_increasing_teams(
                rating, start_index, 1, increasing_cache
            ) + self._count_decreasing_teams(
                rating, start_index, 1, decreasing_cache
            )

        return teams

    def _count_increasing_teams(
        self,
        rating: List[int],
        current_index: int,
        team_size: int,
        increasing_cache: List[List[int]],
    ) -> int:
        n = len(rating)

        # Base case: reached end of array
        if current_index == n:
            return 0

        # Base case: found a valid team of size 3
        if team_size == 3:
            return 1

        # Return cached result if available
        if increasing_cache[current_index][team_size] != -1:
            return increasing_cache[current_index][team_size]

        valid_teams = 0

        # Recursively count teams with increasing ratings
        for next_index in range(current_index + 1, n):
            if rating[next_index] > rating[current_index]:
                valid_teams += self._count_increasing_teams(
                    rating, next_index, team_size + 1, increasing_cache
                )

        # Cache and return the result
        increasing_cache[current_index][team_size] = valid_teams
        return valid_teams

    def _count_decreasing_teams(
        self,
        rating: List[int],
        current_index: int,
        team_size: int,
        decreasing_cache: List[List[int]],
    ) -> int:
        n = len(rating)

        # Base case: reached end of array
        if current_index == n:
            return 0

        # Base case: found a valid team of size 3
        if team_size == 3:
            return 1

        # Return cached result if available
        if decreasing_cache[current_index][team_size] != -1:
            return decreasing_cache[current_index][team_size]

        valid_teams = 0

        # Recursively count teams with decreasing ratings
        for next_index in range(current_index + 1, n):
            if rating[next_index] < rating[current_index]:
                valid_teams += self._count_decreasing_teams(
                    rating, next_index, team_size + 1, decreasing_cache
                )

        # Cache and return the result
        decreasing_cache[current_index][team_size] = valid_teams
        return valid_teams


class Solution3:
    """
    leetcode solution 3: Dynamic Programming (Optimized)
    Runtime: 372 ms, faster than 85.59% of Python3 online submissions for Count Number of Teams.
    Memory Usage: 16.7 MB, less than 66.67% of Python3 online submissions for Count Number of Teams.
    """

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        # Iterate through each soldier as the middle soldier
        for mid in range(n):
            left_smaller = 0
            right_larger = 0

            # Count soldiers with smaller ratings on the left side of the current soldier
            for left in range(mid - 1, -1, -1):
                if rating[left] < rating[mid]:
                    left_smaller += 1

            # Count soldiers with larger ratings on the right side of the current soldier
            for right in range(mid + 1, n):
                if rating[right] > rating[mid]:
                    right_larger += 1

            # Calculate and add the number of ascending rating teams (small-mid-large)
            teams += left_smaller * right_larger

            # Calculate soldiers with larger ratings on the left and smaller ratings on the right
            left_larger = mid - left_smaller
            right_smaller = n - mid - 1 - right_larger

            # Calculate and add the number of descending rating teams (large-mid-small)
            teams += left_larger * right_smaller

        # Return the total number of valid teams
        return teams


class Solution4:
    """
    leetcode solution 4: Binary Indexed Tree (Fenwick Tree)
    Runtime: 120 ms, faster than 94.44% of Python3 online submissions for Count Number of Teams.
    Memory Usage: 17.9 MB, less than 6.25% of Python3 online submissions for Count Number of Teams.
    """

    def numTeams(self, rating: List[int]) -> int:
        # Find the maximum rating
        max_rating = 0
        for r in rating:
            max_rating = max(max_rating, r)

        # Initialize Binary Indexed Trees for left and right sides
        left_BIT = [0] * (max_rating + 1)
        right_BIT = [0] * (max_rating + 1)

        # Populate the right BIT with all ratings initially
        for r in rating:
            self._update_BIT(right_BIT, r, 1)

        teams = 0
        for current_rating in rating:
            # Remove current rating from right BIT
            self._update_BIT(right_BIT, current_rating, -1)

            # Count soldiers with smaller and larger ratings on both sides
            smaller_ratings_left = self._get_prefix_sum(
                left_BIT, current_rating - 1
            )
            smaller_ratings_right = self._get_prefix_sum(
                right_BIT, current_rating - 1
            )
            larger_ratings_left = self._get_prefix_sum(
                left_BIT, max_rating
            ) - self._get_prefix_sum(left_BIT, current_rating)
            larger_ratings_right = self._get_prefix_sum(
                right_BIT, max_rating
            ) - self._get_prefix_sum(right_BIT, current_rating)

            # Count increasing and decreasing sequences
            teams += smaller_ratings_left * larger_ratings_right
            teams += larger_ratings_left * smaller_ratings_right

            # Add current rating to left BIT
            self._update_BIT(left_BIT, current_rating, 1)

        return teams

    # Update the Binary Indexed Tree
    def _update_BIT(self, BIT: List[int], index: int, value: int) -> None:
        while index < len(BIT):
            BIT[index] += value
            index += index & (-index)  # Move to the next relevant index in BIT

    # Get the sum of all elements up to the given index in the BIT
    def _get_prefix_sum(self, BIT: List[int], index: int) -> int:
        psum = 0
        while index > 0:
            psum += BIT[index]
            index -= index & (-index)  # Move to the parent node in BIT
        return psum


class Solution5:
    """
    https://leetcode.com/problems/count-number-of-teams/solution/2545103
    """

    class BIT:
        def __init__(self, n):
            self.tree = [0]*(n+1)
            self.n = n

        def update(self, x, v):
            while x <= self.n:
                self.tree[x] += v
                x += x & -x

        def query(self, x):
            res = 0
            while x > 0:
                res += self.tree[x]
                x -= x & -x
            return res

    def numTeams(self, rating: List[int]) -> int:
        n, N = max(rating), len(rating)

        lbtree = self.BIT(n)
        rbtree = self.BIT(n)
        lbtree.update(rating[0], 1)
        for i in range(1, len(rating)):
            rbtree.update(rating[i], 1)

        res = 0
        for i in range(1, len(rating)-1):
            x = rating[i]
            rbtree.update(x, -1)
            res += rbtree.query(x-1)*(i-lbtree.query(x))
            res += lbtree.query(x-1)*(N-i-1-rbtree.query(x))
            lbtree.update(rating[i], 1)
        return res


class Solution6:
    """
    https://leetcode.com/problems/count-number-of-teams/solution/2545133
    """

    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        count = 0
        for j in range(1, N - 1):
            smaller_left = bigger_left = smaller_right = bigger_right = 0
            for i in range(j):
                smaller_left += rating[i] < rating[j]
                bigger_left += rating[i] > rating[j]
            for k in range(j + 1, N):
                smaller_right += rating[k] < rating[j]
                bigger_right += rating[k] > rating[j]
            count += smaller_left * bigger_right
            count += bigger_left * smaller_right
        return count
