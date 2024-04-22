"""
Leetcode
752. Open the Lock
Medium
2024-04-22

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.

 

Constraints:

    1 <= deadends.length <= 500
    deadends[i].length == 4
    target.length == 4
    target will not be in the list deadends.
    target and deadends[i] consist of digits only.
"""

from collections import deque
from typing import List, Tuple


class Solution:
    """
    Runtime: 364 ms, faster than 82.46% of Python3 online submissions for Open the Lock.
    Memory Usage: 18.4 MB, less than 19.79% of Python3 online submissions for Open the Lock.
    """

    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0

        ends = set()

        for end in deadends:
            ends.add((
                int(end[0]),
                int(end[1]),
                int(end[2]),
                int(end[3])
            ))

        if (0, 0, 0, 0) in ends:
            return -1

        q = [((0, 0, 0, 0), 0)]
        seen = set()
        seen.add((0, 0, 0, 0))

        while q:
            nxt_q = []

            for node, distance in q:
                for nxt in self.closest(node):
                    if nxt in ends or nxt in seen:
                        continue

                    cur_dist = distance + 1

                    if "".join(map(str, nxt)) == target:
                        return cur_dist

                    seen.add(nxt)
                    nxt_q.append((nxt, cur_dist))

            q = nxt_q

        return -1

    def closest(self, val: Tuple[int, int, int, int]):
        val_list = list(val)

        for i in range(4):
            for add in [9, 11]:
                nxt_val = val_list[:]
                nxt_val[i] = (nxt_val[i] + add) % 10
                yield tuple(nxt_val)


class Solution1:
    """
    leetcode solution
    Runtime: 317 ms, faster than 85.77% of Python3 online submissions for Open the Lock.
    Memory Usage: 18 MB, less than 80.21% of Python3 online submissions for Open the Lock.
    """

    def openLock(self, deadends: List[str], target: str) -> int:
        # Map the next slot digit for each current slot digit.
        next_slot = {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "0",
        }
        # Map the previous slot digit for each current slot digit.
        prev_slot = {
            "0": "9",
            "1": "0",
            "2": "1",
            "3": "2",
            "4": "3",
            "5": "4",
            "6": "5",
            "7": "6",
            "8": "7",
            "9": "8",
        }

        # Set to store visited and dead-end combinations.
        visited_combinations = set(deadends)
        # Queue to store combinations generated after each turn.
        pending_combinations = deque()

        # Count the number of wheel turns made.
        turns = 0

        # If the starting combination is also a dead-end,
        # then we can't move from the starting combination.
        if "0000" in visited_combinations:
            return -1

        # Start with the initial combination '0000'.
        pending_combinations.append("0000")
        visited_combinations.add("0000")

        while pending_combinations:
            # Explore all combinations of the current level.
            curr_level_nodes_count = len(pending_combinations)
            for _ in range(curr_level_nodes_count):
                # Get the current combination from the front of the queue.
                current_combination = pending_combinations.popleft()

                # If the current combination matches the target,
                # return the number of turns/level.
                if current_combination == target:
                    return turns

                # Explore all possible new combinations
                # by turning each wheel in both directions.
                for wheel in range(4):
                    # Generate the new combination
                    # by turning the wheel to the next digit.
                    new_combination = list(current_combination)
                    new_combination[wheel] = next_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)
                    # If the new combination is not a dead-end and
                    # was never visited,
                    # add it to the queue and mark it as visited.
                    if new_combination_str not in visited_combinations:
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)

                    # Generate the new combination
                    # by turning the wheel to the previous digit.
                    new_combination = list(current_combination)
                    new_combination[wheel] = prev_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)
                    # If the new combination is not a dead-end and
                    # is never visited,
                    # add it to the queue and mark it as visited.
                    if new_combination_str not in visited_combinations:
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)

            # We will visit next-level combinations.
            turns += 1

        # We never reached the target combination.
        return -1


class Solution2:
    """
    https://leetcode.com/problems/open-the-lock/solution/2362673
    Runtime: 382 ms, faster than 80.21% of Python3 online submissions for Open the Lock.
    Memory Usage: 18 MB, less than 50.54% of Python3 online submissions for Open the Lock.
    """

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if target in deadends:
            return -1
        if '0000' in deadends:
            return -1
        queue = deque(['0000'])
        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return level
                for i in range(4):
                    pre = node[:i]
                    post = node[i + 1:]
                    for op in [-1, 1]:
                        nxt = pre + str((int(node[i]) + op) % 10) + post
                        if nxt not in deadends:
                            deadends.add(nxt)
                            queue.append(nxt)
            level += 1
        return -1
