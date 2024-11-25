"""
Leetcode
2024-11-25
773. Sliding Puzzle
Hard

On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

Example 1:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Example 2:

Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Example 3:

Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

 

Constraints:

    board.length == 2
    board[i].length == 3
    0 <= board[i][j] <= 5
    Each value board[i][j] is unique.

Hints:
- Perform a breadth-first-search, where the nodes are the puzzle boards and edges are if two puzzle boards can be transformed into one another with one move.
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime: 7 ms, faster than 71.16% of Python3 online submissions for Sliding Puzzle.
    Memory Usage: 16.8 MB, less than 52.79% of Python3 online submissions for Sliding Puzzle.
    """

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = board[0] + board[1]
        start = [1, 2, 3, 4, 5, 0]

        if target == start:
            return 0

        q = deque([start])
        seen = set()
        seen.add(self.bhash(start))
        moves = 1

        while q:
            for _ in range(len(q)):
                cur_board = q.popleft()
                for swap in self.swaps(cur_board):
                    bhash = self.bhash(swap)
                    if bhash in seen:
                        continue
                    if swap == target:
                        return moves
                    seen.add(bhash)
                    q.append(swap)
            moves += 1

        return -1

    def bhash(self, board: List[int]):
        n = 0
        for num in board:
            n = (n * 10) + num
        return n

    def swaps(self, board: List[int]):
        i = board.index(0)

        # vertical swap
        swap = board[:]
        si = (i + 3) % 6
        swap[i], swap[si] = swap[si], swap[i]
        yield swap

        # horizontal swap left
        if i % 3 != 0:
            swap = board[:]
            swap[i], swap[i-1] = swap[i-1], swap[i]
            yield swap

        # horizontal swap right
        if i % 3 != 2:
            swap = board[:]
            swap[i], swap[i+1] = swap[i+1], swap[i]
            yield swap


class Solution1:
    """
    leetcode solution 1: Depth-First Search (DFS)
    Runtime: 362 ms, faster than 5.02% of Python3 online submissions for Sliding Puzzle.
    Memory Usage: 17.4 MB, less than 11.88% of Python3 online submissions for Sliding Puzzle.
    """

    # Direction map for zero's possible moves in a flattened 1D array (2x3 board)
    directions = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [3, 5, 1],
        [4, 2],
    ]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Helper method to swap characters at indices i and j in the string
        def _swap(s, i, j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)

        # Convert the 2D board into a string representation to use as state
        start_state = "".join(str(num) for row in board for num in row)

        # Dictionary to store the minimum moves for each visited state
        visited = {}

        def _dfs(state, zero_pos, moves):
            # Skip if this state has been visited with fewer or equal moves
            if state in visited and visited[state] <= moves:
                return
            visited[state] = moves

            # Try moving zero to each possible adjacent position
            for next_pos in self.directions[zero_pos]:
                new_state = _swap(
                    state, zero_pos, next_pos
                )  # Swap to generate new state
                _dfs(
                    new_state, next_pos, moves + 1
                )  # Recursive DFS with updated state and move count

        # Start DFS traversal from initial board state
        _dfs(start_state, start_state.index("0"), 0)

        # Return the minimum moves required to reach the target state, or -1 if unreachable
        return visited.get("123450", -1)


class Solution2:
    """
    leetcode solution 2: Breadth-First Search (BFS)
    Runtime: 5 ms, faster than 79.37% of Python3 online submissions for Sliding Puzzle.
    Memory Usage: 16.7 MB, less than 78.59% of Python3 online submissions for Sliding Puzzle.
    """

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Direction map for zero's possible moves in a 1D representation of the 2x3 board
        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]

        # Helper method to swap characters at indices i and j in the string
        def _swap(state, i, j):
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            return "".join(state_list)

        target = "123450"
        start_state = "".join(str(num) for row in board for num in row)

        visited = set()  # To store visited states
        queue = deque([start_state])
        visited.add(start_state)

        moves = 0

        # BFS to find the minimum number of moves
        while queue:
            for _ in range(len(queue)):
                current_state = queue.popleft()

                # Check if we reached the target solved state
                if current_state == target:
                    return moves

                zero_pos = current_state.index("0")
                for new_pos in directions[zero_pos]:
                    next_state = _swap(current_state, zero_pos, new_pos)

                    # Skip if this state has been visited
                    if next_state in visited:
                        continue

                    # Mark the new state as visited and add it to the queue
                    visited.add(next_state)
                    queue.append(next_state)
            moves += 1

        return -1
