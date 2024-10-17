"""
Leetcode
2024-10-17
670. Maximum Swap
Medium

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

 

Constraints:

    0 <= num <= 10^8
"""


class Solution:
    """
    Runtime: 35 ms, faster than 51.70% of Python3 online submissions for Maximum Swap.
    Memory Usage: 16.5 MB, less than 42.30% of Python3 online submissions for Maximum Swap.
    """

    def maximumSwap(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        n = len(digits)

        for left, cur_d in enumerate(digits):
            swap_d = cur_d
            swap_i = left

            for right in range(left + 1, n):
                nxt_num = digits[right]
                if nxt_num >= swap_d:
                    swap_d, swap_i = nxt_num, right

            if swap_d != cur_d and swap_i != left:
                digits[left], digits[swap_i] = digits[swap_i], digits[left]
                break

        return int("".join([str(d) for d in digits]))


class Solution4:
    """
    leetcode solution 4: Space Optimized Greedy
    Runtime: 43 ms, faster than 5.28% of Python3 online submissions for Maximum Swap.
    Memory Usage: 16.5 MB, less than 79.76% of Python3 online submissions for Maximum Swap.
    """

    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        max_digit_index = -1
        swap_idx_1 = -1
        swap_idx_2 = -1

        # Traverse the string from right to left, tracking the max digit and
        # potential swap
        for i in range(n - 1, -1, -1):
            if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
                max_digit_index = i  # Update the index of the max digit
            elif num_str[i] < num_str[max_digit_index]:
                swap_idx_1 = i  # Mark the smaller digit for swapping
                swap_idx_2 = (
                    max_digit_index  # Mark the larger digit for swapping
                )

        # Perform the swap if a valid swap is found
        if swap_idx_1 != -1 and swap_idx_2 != -1:
            num_str[swap_idx_1], num_str[swap_idx_2] = (
                num_str[swap_idx_2],
                num_str[swap_idx_1],
            )

        return int(
            "".join(num_str)
        )  # Return the new number or the original if no
        # swap occurred


s = Solution()
tests = [
    (98368,
     98863),
]
for inp, exp in tests:
    res = s.maximumSwap(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
