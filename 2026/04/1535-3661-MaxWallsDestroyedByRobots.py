"""
Leetcode
2026-04-03
3661. Maximum Walls Destroyed by Robots
Hard


There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:

    robots[i] is the position of the ith robot.
    distance[i] is the maximum distance the ith robot's bullet can travel.
    walls[j] is the position of the jth wall.

Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.

Return the maximum number of unique walls that can be destroyed by the robots.

Notes:

    A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.
    Robots are not destroyed by bullets.

 

Example 1:

Input: robots = [4], distance = [3], walls = [1,10]

Output: 1

Explanation:

    robots[0] = 4 fires left with distance[0] = 3, covering [1, 4] and destroys walls[0] = 1.
    Thus, the answer is 1.

Example 2:

Input: robots = [10,2], distance = [5,1], walls = [5,2,7]

Output: 3

Explanation:

    robots[0] = 10 fires left with distance[0] = 5, covering [5, 10] and destroys walls[0] = 5 and walls[2] = 7.
    robots[1] = 2 fires left with distance[1] = 1, covering [1, 2] and destroys walls[1] = 2.
    Thus, the answer is 3.

Example 3:

Input: robots = [1,2], distance = [100,1], walls = [10]

Output: 0

Explanation:

In this example, only robots[0] can reach the wall, but its shot to the right is blocked by robots[1]; thus the answer is 0.

 

Constraints:

    1 <= robots.length == distance.length <= 10^5
    1 <= walls.length <= 10^5
    1 <= robots[i], walls[j] <= 10^9
    1 <= distance[i] <= 10^5
    All values in robots are unique
    All values in walls are unique


Hint 1
Sort both the robots and walls arrays. This will help in efficiently processing positions and performing range queries.
Hint 2
Each robot can shoot either left or right. However, if a robot fires and another robot is in its path, the bullet stops. You need to use the positions of neighboring robots to limit the shooting range.
Hint 3
Use binary search (lower_bound and upper_bound) to count how many walls fall within a certain range.
Hint 4
You can use dynamic programming to keep track of the maximum number of walls destroyed so far, depending on the direction the previous robot shot.
"""

import bisect
from typing import List


class Solution1:
    """
    leetcode solution 1: Binary Search + Dynamic Programming
    Runtime 747ms Beats 48.02%
    Memory 48.85MB Beats 99.52%
    """

    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        left = [0] * n
        right = [0] * n
        num = [0] * n
        robots_to_distance = {}

        for i in range(n):
            robots_to_distance[robots[i]] = distance[i]

        robots.sort()
        walls.sort()

        for i in range(n):
            pos1 = bisect.bisect_right(walls, robots[i])

            if i >= 1:
                left_bound = max(
                    robots[i] - robots_to_distance[robots[i]], robots[i - 1] + 1
                )
                left_pos = bisect.bisect_left(walls, left_bound)
            else:
                left_pos = bisect.bisect_left(
                    walls, robots[i] - robots_to_distance[robots[i]]
                )

            left[i] = pos1 - left_pos

            if i < n - 1:
                right_bound = min(
                    robots[i] + robots_to_distance[robots[i]], robots[i + 1] - 1
                )
                right_pos = bisect.bisect_right(walls, right_bound)
            else:
                right_pos = bisect.bisect_right(
                    walls, robots[i] + robots_to_distance[robots[i]]
                )

            pos2 = bisect.bisect_left(walls, robots[i])
            right[i] = right_pos - pos2

            if i == 0:
                continue

            pos3 = bisect.bisect_left(walls, robots[i - 1])
            num[i] = pos1 - pos3

        sub_left, sub_right = left[0], right[0]
        for i in range(1, n):
            current_left = max(
                sub_left + left[i],
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i]),
            )
            current_right = max(sub_left + right[i], sub_right + right[i])
            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)


class Solution2:
    """
    leetcode solution 2: Two Pointers + Dynamic Programming
    Runtime 576ms Beats 75.94%
    Memory 48.56MB Beats 99.52%
    """

    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        left = [0] * n
        right = [0] * n
        num = [0] * n
        robots_to_distance = {}

        for i in range(n):
            robots_to_distance[robots[i]] = distance[i]

        robots.sort()
        walls.sort()

        m = len(walls)
        right_ptr = left_ptr = cur_ptr = robot_ptr = 0

        for i in range(n):
            while right_ptr < m and walls[right_ptr] <= robots[i]:
                right_ptr += 1
            pos1 = right_ptr

            while cur_ptr < m and walls[cur_ptr] < robots[i]:
                cur_ptr += 1
            pos2 = cur_ptr

            if i >= 1:
                left_bound = max(
                    robots[i] - robots_to_distance[robots[i]], robots[i - 1] + 1
                )
            else:
                left_bound = robots[i] - robots_to_distance[robots[i]]

            while left_ptr < m and walls[left_ptr] < left_bound:
                left_ptr += 1
            left_pos = left_ptr
            left[i] = pos1 - left_pos

            if i < n - 1:
                right_bound = min(
                    robots[i] + robots_to_distance[robots[i]], robots[i + 1] - 1
                )
            else:
                right_bound = robots[i] + robots_to_distance[robots[i]]

            while right_ptr < m and walls[right_ptr] <= right_bound:
                right_ptr += 1
            right_pos = right_ptr
            right[i] = right_pos - pos2

            if i == 0:
                continue

            while robot_ptr < m and walls[robot_ptr] < robots[i - 1]:
                robot_ptr += 1
            pos3 = robot_ptr
            num[i] = pos1 - pos3

        sub_left, sub_right = left[0], right[0]
        for i in range(1, n):
            current_left = max(
                sub_left + left[i],
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i]),
            )
            current_right = max(sub_left + right[i], sub_right + right[i])
            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)


class Solution3:
    """
    leetcode solution 3: Two Pointers + Dynamic Programming + Space Optimization
    Runtime 524ms Beats 84.36%
    Memory 48.44MB Beats 99.52%
    """

    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        robot_dist = list(zip(robots, distance))
        robot_dist.sort(key=lambda x: x[0])
        walls.sort()

        m = len(walls)
        right_ptr = left_ptr = cur_ptr = robot_ptr = 0

        prev_left = prev_right = prev_num = 0
        sub_left = sub_right = 0

        for i in range(n):
            robot_pos, robot_dist_val = robot_dist[i]

            while right_ptr < m and walls[right_ptr] <= robot_pos:
                right_ptr += 1
            pos1 = right_ptr

            while cur_ptr < m and walls[cur_ptr] < robot_pos:
                cur_ptr += 1
            pos2 = cur_ptr

            if i >= 1:
                left_bound = max(
                    robot_pos - robot_dist_val, robot_dist[i - 1][0] + 1
                )
            else:
                left_bound = robot_pos - robot_dist_val

            while left_ptr < m and walls[left_ptr] < left_bound:
                left_ptr += 1
            left_pos = left_ptr
            current_left = pos1 - left_pos

            if i < n - 1:
                right_bound = min(
                    robot_pos + robot_dist_val, robot_dist[i + 1][0] - 1
                )
            else:
                right_bound = robot_pos + robot_dist_val

            while right_ptr < m and walls[right_ptr] <= right_bound:
                right_ptr += 1
            right_pos = right_ptr
            current_right = right_pos - pos2

            current_num = 0
            if i > 0:
                while robot_ptr < m and walls[robot_ptr] < robot_dist[i - 1][0]:
                    robot_ptr += 1
                pos3 = robot_ptr
                current_num = pos1 - pos3

            if i == 0:
                sub_left = current_left
                sub_right = current_right
            else:
                new_sub_left = max(
                    sub_left + current_left,
                    sub_right
                    - prev_right
                    + min(current_left + prev_right, current_num),
                )
                new_sub_right = max(
                    sub_left + current_right, sub_right + current_right
                )
                sub_left = new_sub_left
                sub_right = new_sub_right

            prev_left = current_left
            prev_right = current_right
            prev_num = current_num

        return max(sub_left, sub_right)
