"""
Leetcode
2025-02-19
2375. Construct Smallest Number From DI String
Solved
Medium
Topics
Companies
Hint

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

    num consists of the digits '1' to '9', where each digit is used at most once.
    If pattern[i] == 'I', then num[i] < num[i + 1].
    If pattern[i] == 'D', then num[i] > num[i + 1].

Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.

Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.

 

Constraints:

    1 <= pattern.length <= 8
    pattern consists of only the letters 'I' and 'D'.

Hint 1
With the constraints, could we generate every possible string?
Hint 2
Yes we can. Now we just need to check if the string meets all the conditions.
"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.92MB Beats 16.84%
    """

    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        used = [False] * 10
        ans = []

        def dfs(pos: int):
            if pos >= n:
                return True

            for i in range(1, 10):
                if used[i]:
                    continue

                is_valid = not ans \
                    or (pattern[pos] == "I" and i > ans[-1]) \
                    or (pattern[pos] == "D" and i < ans[-1])
                if not is_valid:
                    continue

                ans.append(i)
                used[i] = True
                if dfs(pos + 1):
                    return True
                ans.pop()
                used[i] = False

            return False

        dfs(-1)
        return "".join(str(d) for d in ans)


class Solution3:
    """
    leetcode solution 3: Regulated Brute Force via Recursion
    """

    result = []

    def smallestNumber(self, pattern: str) -> str:
        self.result = []

        # Start building the sequence by calling the helper function
        self.build_sequence(0, 0, pattern)
        # Reverse the final result
        return "".join(self.result[::-1])

    # Recursively build the sequence
    def build_sequence(
        self, current_index: int, current_count: int, pattern: str
    ) -> int:
        if current_index != len(pattern):
            if pattern[current_index] == "I":
                # If 'I', increment the count and move to the next index
                self.build_sequence(
                    current_index + 1, current_index + 1, pattern
                )
            else:
                # If 'D', keep the count and move to the next index
                current_count = self.build_sequence(
                    current_index + 1, current_count, pattern
                )

        self.result.append(str(current_count + 1))

        # Return the next count for the sequence
        return current_count + 1


class Solution4:
    """
    leetcode solution 4: Using Stack
    """

    def smallestNumber(self, pattern: str) -> str:
        result = []
        num_stack = []

        # Iterate through the pattern
        for index in range(len(pattern) + 1):
            # Push the next number onto the stack
            num_stack.append(index + 1)

            # If 'I' is encountered or we reach the end, pop all stack elements
            if index == len(pattern) or pattern[index] == "I":
                while num_stack:
                    result.append(str(num_stack.pop()))

        return "".join(result)


class Solution5:
    """
    leetcode solution 5: Greedy Approach with Sliding Window Reversal
    """

    def smallestNumber(self, pattern: str) -> str:
        result = []

        # Iterate through the pattern and build the result
        previous_index = 0
        for current_index in range(len(pattern) + 1):
            result.append(str(1 + current_index))

            # Reverse the substring starting from previous_index when necessary
            if current_index == len(pattern) or pattern[current_index] == "I":
                result[previous_index:] = reversed(result[previous_index:])
                previous_index = current_index + 1

        return "".join(result)


class Solution6:
    """
    leetcode solution 6: Optimized Greedy Approach with Precomputed 'D' Segments
    Runtime 0ms Beats 100.00%
    Memory 17.98MB Beats 16.84%
    """

    def smallestNumber(self, pattern: str) -> str:
        pattern_length = len(pattern)
        max_so_far = curr_max = temp = 0

        # List to store lengths of decreasing subsequences in the pattern
        arr_D = [0 for _ in range(pattern_length + 2)]

        # Compute the lengths of decreasing subsequences in the pattern
        for pattern_index in range(pattern_length, -1, -1):
            if pattern_index < pattern_length and pattern[pattern_index] == "D":
                # If 'D', increment the length of the decreasing sequence
                arr_D[pattern_index] = arr_D[pattern_index + 1] + 1
        result = ""

        # Build the result string based on the pattern
        for position in range(pattern_length + 1):
            if position < pattern_length and pattern[position] == "I":
                # If 'I', assign the next maximum digit and append it to the
                # result
                max_so_far += 1
                result += str(max_so_far)

                # Update the max digit encountered so far
                max_so_far = max(max_so_far, curr_max)
                # Reset current max for the next iteration
                curr_max = 0

            else:
                # If 'D', calculate the appropriate digit and append it to the
                # result
                temp = 1 + max_so_far + arr_D[position]
                result += str(temp)

                # Update the current max value
                curr_max = max(curr_max, temp)

        return result
