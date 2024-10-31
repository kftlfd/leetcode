"""
Leetcode
2024-10-31
2463. Minimum Total Distance Traveled
Hard

There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

    All robots move at the same speed.
    If two robots move in the same direction, they will never collide.
    If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
    If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
    If the robot moved from a position x to a position y, the distance it moved is |y - x|.

 

Example 1:

Input: robot = [0,4,6], factory = [[2,2],[6,2]]
Output: 4
Explanation: As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.

Example 2:

Input: robot = [1,-1], factory = [[-2,1],[2,1]]
Output: 2
Explanation: As shown in the figure:
- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.

 

Constraints:

    1 <= robot.length, factory.length <= 100
    factory[j].length == 2
    -10^9 <= robot[i], positionj <= 10^9
    0 <= limitj <= robot.length
    The input will be generated such that it is always possible to repair every robot.

Hints:
- Sort robots and factories by their positions.
- After sorting, notice that each factory should repair some subsegment of robots.
- Find the minimum total distance to repair first i robots with first j factories.    
"""

from typing import List


class Solution2:
    """
    leetcode solution 2: Memoization
    Runtime: 2119 ms, faster than 28.00% of Python3 online submissions for Minimum Total Distance Traveled.
    Memory Usage: 109.9 MB, less than 21.09% of Python3 online submissions for Minimum Total Distance Traveled.
    """

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot = sorted(robot)
        factory = sorted(factory, key=lambda x: x[0])
        factory_positions = []
        for f in factory:
            factory_positions.extend([f[0]] * f[1])
        robot_count = len(robot)
        factory_count = len(factory_positions)

        dp = [[None] * (factory_count + 1) for _ in range(robot_count + 1)]

        def _calculate_min_distance(robot_idx: int, factory_idx: int) -> int:
            if dp[robot_idx][factory_idx] is not None:
                return dp[robot_idx][factory_idx]
            if robot_idx == robot_count:
                dp[robot_idx][factory_idx] = 0
                return 0
            if factory_idx == factory_count:
                dp[robot_idx][factory_idx] = int(1e12)
                return int(1e12)

            assign = abs(
                robot[robot_idx] - factory_positions[factory_idx]
            ) + _calculate_min_distance(robot_idx + 1, factory_idx + 1)

            skip = _calculate_min_distance(robot_idx, factory_idx + 1)

            dp[robot_idx][factory_idx] = min(assign, skip)
            return dp[robot_idx][factory_idx]

        return _calculate_min_distance(0, 0)


class Solution4:
    """
    leetcode solution 4: Space Optimized Tabulation
    Runtime: 940 ms, faster than 80.00% of Python3 online submissions for Minimum Total Distance Traveled.
    Memory Usage: 17.9 MB, less than 67.35% of Python3 online submissions for Minimum Total Distance Traveled.
    """

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots and factories by position
        robots = sorted(robot)
        factories = sorted(factory)

        # Flatten factory positions according to their capacities
        factory_positions = []
        for factory in factories:
            for i in range(factory[1]):
                factory_positions.append(factory[0])

        robot_count = len(robots)
        factory_count = len(factory_positions)
        next_dist = [0 for _ in range(factory_count + 1)]
        current = [0 for _ in range(factory_count + 1)]

        # Fill DP table using two rows for optimization
        for i in range(robot_count - 1, -1, -1):
            # No factories left case
            if i != robot_count - 1:
                next_dist[factory_count] = 1e12

            # Initialize current row
            current[factory_count] = 1e12

            for j in range(factory_count - 1, -1, -1):
                # Assign current robot to current factory
                assign = (
                    abs(robots[i] - factory_positions[j]) + next_dist[j + 1]
                )

                # Skip current factory for this robot
                skip = current[j + 1]
                # Take the minimum option
                current[j] = min(assign, skip)

            # Move to next robot
            next_dist = current[:]

        # Return minimum distance starting from the first robot
        return current[0]
