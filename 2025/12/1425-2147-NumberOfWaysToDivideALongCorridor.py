"""
Leetcode
2025-12-14
2147. Number of Ways to Divide a Long Corridor
Hard

Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.

 

Example 1:

Input: corridor = "SSPPSPS"
Output: 3
Explanation: There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, each section has exactly two seats.

Example 2:

Input: corridor = "PPSPSP"
Output: 1
Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
Installing any would create some section that does not have exactly two seats.

Example 3:

Input: corridor = "S"
Output: 0
Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.

 

Constraints:

    n == corridor.length
    1 <= n <= 10^5
    corridor[i] is either 'S' or 'P'.


Hint 1
Divide the corridor into segments. Each segment has two seats, starts precisely with one seat, and ends precisely with the other seat.
Hint 2
How many dividers can you install between two adjacent segments? You must install precisely one. Otherwise, you would have created a section with not exactly two seats.
Hint 3
If there are k plants between two adjacent segments, there are k + 1 positions (ways) you could install the divider you must install.
Hint 4
The problem now becomes: Find the product of all possible positions between every two adjacent segments.
"""


class Solution:
    """
    Runtime 235ms Beats 89.52%
    Memory 18.06MB Beats 95.24%
    """

    def numberOfWays(self, corridor: str) -> int:
        valid = False
        ans = 1
        seats = 0
        prev = 0
        fullRoom = False
        MOD = 10**9 + 7

        for i, c in enumerate(corridor):
            if c != "S":
                continue
            if seats == 2:
                ans = ans * (i - prev) % MOD
                seats = 0
                prev = i
                fullRoom = False
                valid = False
            seats += 1
            if seats == 2 and not fullRoom:
                prev = i
                fullRoom = True
                valid = True

        return ans if valid else 0


class Solution1:
    """
    leetcode solution 1: Top-Down Dynamic Programming
    Runtime 2527ms Beats 9.52%
    Memory 52.44MB Beats 19.05%
    """

    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Cache the result of each sub-problem
        cache = [[-1] * 3 for _ in range(len(corridor))]

        # Count the number of ways to divide from "index" to the last index
        # with "seats" number of "S" in the current section
        def count(index, seats):
            # If we have reached the end of the corridor, then
            # the current section is valid only if "seats" is 2
            if index == len(corridor):
                return 1 if seats == 2 else 0

            # If we have already computed the result of this sub-problem,
            # then return the cached result
            if cache[index][seats] != -1:
                return cache[index][seats]

            # If the current section has exactly 2 "S"
            if seats == 2:
                # If the current element is "S", then we have to close the
                # section and start a new section from this index. Next index
                # will have one "S" in the current section
                if corridor[index] == "S":
                    result = count(index + 1, 1)
                else:
                    # If the current element is "P", then we have two options
                    # 1. Close the section and start a new section from this index
                    # 2. Keep growing the section
                    result = (count(index + 1, 0) + count(index + 1, 2)) % MOD
            else:
                # Keep growing the section. Increment "seats" if present
                # element is "S"
                if corridor[index] == "S":
                    result = count(index + 1, seats + 1)
                else:
                    result = count(index + 1, seats)

            # Memoize the result, and return it
            cache[index][seats] = result
            return cache[index][seats]

        # Call the count function
        return count(0, 0)


class Solution2:
    """
    leetcode solution 2: Bottom-up Dynamic Programming
    Runtime 1533ms Beats 18.09%
    Memory 31.65MB Beats 21.90%
    """

    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Initialize the array to store the result of each sub-problem
        count = [[-1] * 3 for _ in range(len(corridor) + 1)]

        # Base cases
        count[len(corridor)][0] = 0
        count[len(corridor)][1] = 0
        count[len(corridor)][2] = 1

        # Fill the array in a bottom-up fashion
        for index in range(len(corridor) - 1, -1, -1):
            if corridor[index] == "S":
                count[index][0] = count[index + 1][1]
                count[index][1] = count[index + 1][2]
                count[index][2] = count[index + 1][1]
            else:
                count[index][0] = count[index + 1][0]
                count[index][1] = count[index + 1][1]
                count[index][2] = (count[index + 1][0] +
                                   count[index + 1][2]) % MOD

        # Return the result
        return count[0][0]


class Solution3:
    """
    leetcode solution 3: Space-Optimized Bottom-up Dynamic Programming
    Runtime 175ms Beats 96.19%
    Memory 18.09MB Beats 95.24%
    """

    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Initial values of three variables
        zero = 0
        one = 0
        two = 1

        # Compute using derived equations
        for thing in corridor:
            if thing == "S":
                zero = one
                one, two = two, one
            else:
                two = (two + zero) % MOD

        # Return the result
        return zero


class Solution4:
    """
    leetcode solution 4: Combinatorics
    Runtime 279ms Beats 57.14%
    Memory 22.41MB Beats 47.62%
    """

    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Store indices of S in an array
        indices = []
        for i, thing in enumerate(corridor):
            if thing == "S":
                indices.append(i)

        # When division is not possible
        if indices == [] or len(indices) % 2 == 1:
            return 0

        # Total number of ways
        count = 1

        # Take the product of non-paired neighbors
        previous_pair_last = 1
        current_pair_first = 2
        while current_pair_first < len(indices):
            count *= (indices[current_pair_first] -
                      indices[previous_pair_last])
            count %= MOD
            previous_pair_last += 2
            current_pair_first += 2

        # Return the number of ways
        return count


class Solution5:
    """
    leetcode solution 5: Combinatorics, Space Optimized
    Runtime 241ms Beats 85.71%
    Memory 18.05MB Beats 95.24%
    """

    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Total number of ways
        count = 1

        # Number of seats in current section
        seats = 0

        # Tracking Index of last S in the previous section
        previous_pair_last = None

        # Keep track of seats in the corridor
        for index, thing in enumerate(corridor):
            if thing == "S":
                seats += 1

                # If two seats, then this is the last S in the section
                # Update seats for the next section
                if seats == 2:
                    previous_pair_last = index
                    seats = 0

                # If one seat, then this is the first S in the section
                # Compute the product of non-paired neighbors
                elif seats == 1 and previous_pair_last is not None:
                    count *= (index - previous_pair_last)
                    count %= MOD

        # If odd seats, or zero seats
        if seats == 1 or previous_pair_last is None:
            return 0

        # Return the number of ways
        return count
