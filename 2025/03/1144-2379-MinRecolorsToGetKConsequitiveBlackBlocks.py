"""
Leetcode
2025-03-08
2379. Minimum Recolors to Get K Consecutive Black Blocks
Easy

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

 

Constraints:

    n == blocks.length
    1 <= n <= 100
    blocks[i] is either 'W' or 'B'.
    1 <= k <= n


Hint 1
Iterate through all possible consecutive substrings of k characters.
Hint 2
Find the number of changes for each substring to make all blocks black, and return the minimum of these.
"""


class Solution:
    """
    Runtime 4ms Beats 15.26%
    Memory 17.62MB Beats 88.78%
    """

    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks = [c == "W" for c in blocks]
        window = sum(blocks[:k])
        ans = window

        for i in range(k, len(blocks)):
            window += blocks[i] - blocks[i - k]
            ans = min(ans, window)

        return ans


class Solution2:
    """
    leetcode solution 2: Sliding Window
    Runtime 0ms Beats 100.00%
    Memory 17.57MB Beats 98.20%
    """

    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        num_whites = 0
        num_recolors = float("inf")

        # Move right pointer
        for right in range(len(blocks)):

            # Increment num_whites if block at right pointer is white
            if blocks[right] == "W":
                num_whites += 1

            # k consecutive elements are found
            if right - left + 1 == k:

                # Update minimum
                num_recolors = min(num_recolors, num_whites)

                # Decrement num_whites if block at left pointer is white
                if blocks[left] == "W":
                    num_whites -= 1

                # Move left pointer
                left += 1

        return num_recolors
