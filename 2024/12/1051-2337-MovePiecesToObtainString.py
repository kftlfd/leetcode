"""
Leetcode
2024-12-05
2337. Move Pieces to Obtain a String
Medium

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

    The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
    The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.

Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

 

Example 1:

Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.

Example 2:

Input: start = "R_L_", target = "__LR"
Output: false
Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.

Example 3:

Input: start = "_R", target = "R_"
Output: false
Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.

 

Constraints:

    n == start.length == target.length
    1 <= n <= 10^5
    start and target consist of the characters 'L', 'R', and '_'.
"""


class Solution:
    """
    Time Limit Exceeded
    """

    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i = 0
        start = list(start)

        while i < n:
            cur_c, cur_t = start[i], target[i]

            if cur_c == cur_t:
                i += 1
                continue

            if cur_t == "R":
                return False

            swap_i = i
            ok = False
            fails = "L" if cur_t == "_" else "R"
            while swap_i < n:
                if start[swap_i] == fails:
                    break
                if start[swap_i] == cur_t:
                    start[i], start[swap_i] = start[swap_i], start[i]
                    ok = True
                    break
                swap_i += 1
            if not ok:
                return False

            i += 1

        return True


class Solution1:
    """
    leetcode solution
    Runtime: 112 ms, faster than 78.23% of Python3 online submissions for Move Pieces to Obtain a String.
    Memory Usage: 17.8 MB, less than 37.72% of Python3 online submissions for Move Pieces to Obtain a String.
    """

    def canChange(self, start: str, target: str) -> bool:
        start_length = len(start)
        # pointers for start string and target string
        start_index, target_index = (0, 0)

        while start_index < start_length or target_index < start_length:
            # skip underscores in start
            while start_index < start_length and start[start_index] == "_":
                start_index += 1

            # skip underscores in target
            while target_index < start_length and target[target_index] == "_":
                target_index += 1

            # if one string exhausted, both strings should be exhausted
            if start_index == start_length or target_index == start_length:
                return (
                    start_index == start_length and target_index == start_length
                )

            # check if the pieces match and follow movement rules
            if (
                start[start_index] != target[target_index]
                or (start[start_index] == "L" and start_index < target_index)
                or (start[start_index] == "R" and start_index > target_index)
            ):
                return False

            start_index += 1
            target_index += 1

        # if all conditions satisfied, return true
        return True
