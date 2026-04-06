"""
Leetcode
2026-04-06
874. Walking Robot Simulation
Medium

A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot receives an array of integers commands, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:

    -2: Turn left 90 degrees.
    -1: Turn right 90 degrees.
    1 <= k <= 9: Move forward k units, one unit at a time.

Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).

Note:

    There can be an obstacle at (0, 0). If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to (0, 0) due to the obstacle.
    North means +Y direction.
    East means +X direction.
    South means -Y direction.
    West means -X direction.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []

Output: 25

Explanation:

The robot starts at (0, 0):

    Move north 4 units to (0, 4).
    Turn right.
    Move east 3 units to (3, 4).

The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.

Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]

Output: 65

Explanation:

The robot starts at (0, 0):

    Move north 4 units to (0, 4).
    Turn right.
    Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
    Turn left.
    Move north 4 units to (1, 8).

The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.

Example 3:

Input: commands = [6,-1,-1,6], obstacles = [[0,0]]

Output: 36

Explanation:

The robot starts at (0, 0):

    Move north 6 units to (0, 6).
    Turn right.
    Turn right.
    Move south 5 units and get blocked by the obstacle at (0,0), robot is at (0, 1).

The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.

 

Constraints:

    1 <= commands.length <= 10^4
    commands[i] is either -2, -1, or an integer in the range [1, 9].
    0 <= obstacles.length <= 10^4
    -3 * 10^4 <= xi, yi <= 3 * 10^4
    The answer is guaranteed to be less than 2^31.


"""

from typing import List


class Solution:
    """
    Runtime 25ms Beats 91.23%
    Memory 23.79MB Beats 69.44%
    """

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = y = 0
        dirs = (
            (0, 1),  # up
            (1, 0),  # right
            (0, -1),  # down
            (-1, 0),  # left
        )
        cur_dir = 0
        max_sq_dist = 0
        obst = {(x, y) for x, y in obstacles}

        for command in commands:
            if command == -1:
                # turn right
                cur_dir = (cur_dir + 1) % 4
            elif command == -2:
                # turn left
                cur_dir = (cur_dir + 3) % 4
            else:
                dx, dy = dirs[cur_dir]
                for _ in range(command):
                    if (x+dx, y+dy) in obst:
                        break
                    x += dx
                    y += dy
                max_sq_dist = max(max_sq_dist, x*x + y*y)

        return max_sq_dist


class Solution1:
    """
    leetcode solution: Simulation
    Runtime 28ms Beats 83.81%
    Memory 23.70MB Beats 69.44%
    """

    def __init__(self):
        self.HASH_MULTIPLIER = (
            60013  # Slightly larger than 2 * max coordinate value
        )

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Store obstacles in an set for efficient lookup
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}

        # Define direction vectors: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        max_distance_squared = 0
        current_direction = 0  # 0: North, 1: East, 2: South, 3: West

        for command in commands:
            if command == -1:  # Turn right
                current_direction = (current_direction + 1) % 4
                continue

            if command == -2:  # Turn left
                current_direction = (current_direction + 3) % 4
                continue

            # Move forward
            dx, dy = directions[current_direction]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if self._hash_coordinates(next_x, next_y) in obstacle_set:
                    break
                x, y = next_x, next_y

            max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared

    # Hash function to convert (x, y) coordinates to a unique integer value
    def _hash_coordinates(self, x: int, y: int) -> int:
        return x + self.HASH_MULTIPLIER * y
