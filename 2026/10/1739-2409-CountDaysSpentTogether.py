"""
Leetcode
2026-10-24
2409. Count Days Spent Together
Easy

Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

 

Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

 

Constraints:

    All dates are provided in the format "MM-DD".
    Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
    The given dates are valid dates of a non-leap year.

 
Hint 1
For a given day, determine if Alice or Bob or both are in Rome.
Hint 2
Brute force all 365 days for both Alice and Bob.
"""


class Solution:
    """
    Runtime 1ms Beats 15.23%
    Memory 19.36MB Beats 47.27%
    """

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def parse(datestr: str) -> int:
            return sum(m[:int(datestr[:2])]) + int(datestr[3:])

        a = (parse(arriveAlice), parse(leaveAlice))
        b = (parse(arriveBob), parse(leaveBob))

        if b[0] < a[0]:
            a, b = b, a

        return max(0, min(a[1], b[1]) - b[0] + 1)


class Solution1:
    """
    leetcode solution: Convert Dates to Days of the Year and Calculate the Difference
    Runtime 0ms Beats 100.00%
    Memory 19.26MB Beats 79.30%
    """

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        datesOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefixSum = [0]
        for date in datesOfMonths:
            prefixSum.append(prefixSum[-1] + date)

        arriveAliceDay = self.calculateDayOfYear(arriveAlice, prefixSum)
        leaveAliceDay = self.calculateDayOfYear(leaveAlice, prefixSum)
        arriveBobDay = self.calculateDayOfYear(arriveBob, prefixSum)
        leaveBobDay = self.calculateDayOfYear(leaveBob, prefixSum)
        return max(
            0,
            min(leaveAliceDay, leaveBobDay)
            - max(arriveAliceDay, arriveBobDay)
            + 1,
        )

    def calculateDayOfYear(self, day: str, prefixSum: list[int]) -> int:
        month = int(day[:2])
        date = int(day[3:])
        return prefixSum[month - 1] + date
