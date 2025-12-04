"""
Leetcode
2025-12-04
2211. Count Collisions on a Road
Medium

There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.

The number of collisions can be calculated as follows:

    When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
    When a moving car collides with a stationary car, the number of collisions increases by 1.

After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

Return the total number of collisions that will happen on the road.

 

Example 1:

Input: directions = "RLRSLL"
Output: 5
Explanation:
The collisions that will happen on the road are:
- Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2.
- Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
- Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
- Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get hit by car 5. The number of collisions becomes 4 + 1 = 5.
Thus, the total number of collisions that will happen on the road is 5. 

Example 2:

Input: directions = "LLRR"
Output: 0
Explanation:
No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.

 

Constraints:

    1 <= directions.length <= 10^5
    directions[i] is either 'L', 'R', or 'S'.


Hint 1
In what circumstances does a moving car not collide with another car?
Hint 2
If we disregard the moving cars that do not collide with another car, what does each moving car contribute to the answer?
Hint 3
Will stationary cars contribute towards the answer?
"""


class Solution01:
    """
    Runtime 127ms Beats 50.19%
    Memory 18.14MB Beats 88.10%
    """

    def countCollisions(self, directions: str) -> int:
        start = 0
        end = len(directions) - 1

        while start <= end and directions[start] == "L":
            start += 1
        while end >= start and directions[end] == "R":
            end -= 1

        right = 0
        prev = None
        collisions = 0

        for i in range(start, end + 1):
            cur = directions[i]
            if cur == "R":
                right += 1
                prev = "R"
            elif cur == "S":
                collisions += right
                right = 0
                prev = "S"
            # cur == "L"
            elif prev == "S":
                collisions += 1
            elif prev == "R":
                collisions += right + 1
                right = 0
                prev = "S"

        return collisions


class Solution02:
    """
    Runtime 95ms Beats 62.08%
    Memory 18.39MB Beats 56.88%
    """

    def countCollisions(self, directions: str) -> int:
        collisions = 0
        right = 0
        prev = None

        for cur in directions:
            if cur == "R":
                right += 1
                prev = "R"
            elif cur == "S":
                collisions += right
                right = 0
                prev = "S"
            # cur == "L"
            elif prev == "S":
                collisions += 1
            elif prev == "R":
                collisions += right + 1
                right = 0
                prev = "S"

        return collisions


class Solution1:
    """
    leetcode solution 1: Simulation
    Runtime 86ms Beats 67.29%
    Memory 18.26MB Beats 70.26%
    """

    def countCollisions(self, directions: str) -> int:
        res = 0
        flag = -1

        for c in directions:
            if c == "L":
                if flag >= 0:
                    res += flag + 1
                    flag = 0
            elif c == "S":
                if flag > 0:
                    res += flag
                flag = 0
            else:
                if flag >= 0:
                    flag += 1
                else:
                    flag = 1
        return res


class Solution2:
    """
    leetcode solution 2: Counting
    Runtime 7ms Beats 95.91%
    Memory 18.26MB Beats 70.26%
    """

    def countCollisions(self, directions: str) -> int:
        # Left-moving outward vehicles and right-moving outward vehicles
        # will not collide with anything,
        # All other vehicles will collide exactly once.
        dirs = directions.lstrip("L").rstrip("R")
        return len(dirs) - dirs.count("S")
