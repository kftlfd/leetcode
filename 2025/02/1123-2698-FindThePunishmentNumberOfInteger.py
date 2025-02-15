"""
Leetcode
2025-02-15
2698. Find the Punishment Number of an Integer
Medium
Topics
Companies
Hint

Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

    1 <= i <= n
    The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.

 

Example 1:

Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182

Example 2:

Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478

 

Constraints:

    1 <= n <= 1000


Hint 1
Can we generate all possible partitions of a number?
Hint 2
Use a recursive algorithm that splits the number into two parts, generates all possible partitions of each part recursively, and then combines them in all possible ways.
"""


class Solution01:
    """
    Runtime 1647ms Beats 5.15%
    Memory 17.82MB Beats 55.14%
    """

    def punishmentNumber(self, n: int) -> int:

        def partitions(val: str):
            yield [int(val)]
            for i in range(1, len(val)):
                left = int(val[:i])
                for right in partitions(val[i:]):
                    yield [left] + right

        return sum(
            i * i
            for i in range(1, n + 1)
            if any(sum(p) == i for p in partitions(str(i * i)))
        )


class Solution02:
    """
    Runtime 1124ms Beats 46.86%
    Memory 17.91MB Beats 39.43%
    """

    def punishmentNumber(self, n: int) -> int:

        def is_valid(partition: str, goal_sum: int) -> bool:
            if goal_sum < 0:
                return False

            if int(partition) == goal_sum:
                return True

            return any(
                is_valid(partition[i:], goal_sum - int(partition[:i]))
                for i in range(1, len(partition))
            )

        ans = 0

        for i in range(1, n + 1):
            i_sq = i * i
            if is_valid(str(i_sq), i):
                ans += i_sq

        return ans


class Solution1:
    """
    leetcode solution 1: Memoization
    Runtime 1330ms Beats 22.86%
    Memory 18.17MB Beats 17.14%
    """

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0
        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square_num = current_num * current_num
            string_num = str(square_num)

            # Initialize values in memoization array
            memo_array = [
                [-1] * (current_num + 1) for _ in range(len(string_num))
            ]

            # Check if valid partition can be found and add squared number if so
            if self.find_partitions(0, 0, string_num, current_num, memo_array):
                punishment_num += square_num

        return punishment_num

    def find_partitions(
        self, start_index, current_sum, string_num, target, memo
    ):
        # Check if partition is valid
        if start_index == len(string_num):
            return current_sum == target

        # Invalid partition found, so we return False
        if current_sum > target:
            return False

        # If the result for this state is already calculated, return it
        if memo[start_index][current_sum] != -1:
            return memo[start_index][current_sum] == 1

        partition_found = False

        # Iterate through all possible substrings starting with start_index
        for current_index in range(start_index, len(string_num)):
            # Create partition
            current_string = string_num[start_index: current_index + 1]
            addend = int(current_string)

            # Recursively check if valid partition can be found
            partition_found = partition_found or self.find_partitions(
                current_index + 1,
                current_sum + addend,
                string_num,
                target,
                memo,
            )
            if partition_found:
                memo[start_index][current_sum] = 1
                return True

        # Memoize the result for future reference and return its result
        memo[start_index][current_sum] = 0
        return False


class Solution2:
    """
    leetcode solution 2: Recursion of Strings
    Runtime 1126ms Beats 46.86%
    Memory 17.71MB Beats 68.86%
    """

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square_num = current_num * current_num

            # Check if valid partition can be found and add squared number if so
            if self.can_partition(str(square_num), current_num):
                punishment_num += square_num

        return punishment_num

    def can_partition(self, string_num, target):
        # Valid Partition Found
        if not string_num and target == 0:
            return True

        # Invalid Partition Found
        if target < 0:
            return False

        # Recursively check all partitions for a valid partition
        for index in range(len(string_num)):
            left = string_num[: index + 1]
            right = string_num[index + 1:]
            left_num = int(left)

            if self.can_partition(right, target - left_num):
                return True

        return False


class Solution3:
    """
    leetcode solution 3: Recursion of Integers
    Runtime 87ms Beats 86.57%
    Memory 17.93MB Beats 39.43%
    """

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square_num = current_num * current_num

            # Check if valid partition can be found and add squared number if so
            if self.can_partition(square_num, current_num):
                punishment_num += square_num

        return punishment_num

    def can_partition(self, num, target):
        # Invalid partition found
        if target < 0 or num < target:
            return False

        # Valid partition found
        if num == target:
            return True

        # Recursively check all partitions for a valid partition
        return (
            self.can_partition(num // 10, target - num % 10)
            or self.can_partition(num // 100, target - num % 100)
            or self.can_partition(num // 1000, target - num % 1000)
        )
