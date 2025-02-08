"""
Leetcode
2025-02-08
2349. Design a Number Container System
Medium
Topics
Companies
Hint

Design a number container system that can do the following:

    Insert or Replace a number at the given index in the system.
    Return the smallest index for the given number in the system.

Implement the NumberContainers class:

    NumberContainers() Initializes the number container system.
    void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
    int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.

 

Example 1:

Input
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output
[null, -1, null, null, null, null, 1, null, 2]

Explanation
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.

 

Constraints:

    1 <= index, number <= 10^9
    At most 10^5 calls will be made in total to change and find.

Hint 1
Use a hash table to efficiently map each number to all of its indices in the container and to map each index to their current number.
Hint 2
In addition, you can use ordered set to store all of the indices for each number to solve the find method. Do not forget to update the ordered set according to the change method.
"""

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)


from collections import defaultdict
import heapq

from sortedcontainers import SortedSet


class NumberContainers:
    """
    Time Limit Exceeded
    """

    def __init__(self):
        self.indexes = {}
        self.numbers = defaultdict(set)

    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            self.numbers[self.indexes[index]].remove(index)
        self.indexes[index] = number
        self.numbers[number].add(index)

    def find(self, number: int) -> int:
        if len(self.numbers[number]) < 1:
            return -1
        return min(self.numbers[number])


class NumberContainers1:
    """
    leetcode solution 1: Two Maps
    Runtime 676ms Beats 16.67%
    Memory 151.73MB Beats 14.71%
    """

    def __init__(self):
        # Initializing the defaultdict with SortedSet and the regular dictionary
        # Map from number to set of indices
        self.number_to_indices = defaultdict(SortedSet)
        # Map from index to number
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        # If index already has a number, remove it from the old number's index set
        if index in self.index_to_number:
            previous_number = self.index_to_number[index]
            self.number_to_indices[previous_number].remove(index)
            if not self.number_to_indices[previous_number]:
                del self.number_to_indices[previous_number]

        # Update the number and add the index to the new number's set
        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        # Return the smallest index for the given number, or -1 if not found
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1


class NumberContainers2:
    """
    leetcode solution 2: Using Min Heap with Lazy Update
    Runtime 112ms Beats 77.45%
    Memory 76.44MB Beats 81.37%
    """

    def __init__(self):
        # Map to store number -> min heap of indices
        self.number_to_indices = defaultdict(list)
        # Map to store index -> number
        self.index_to_numbers = {}

    def change(self, index: int, number: int) -> None:
        # Update index to number mapping
        self.index_to_numbers[index] = number

        # Add index to the min heap for this number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        # If number doesn't exist in our map
        if not self.number_to_indices[number]:
            return -1

        # Keep checking top element until we find valid index
        while self.number_to_indices[number]:
            index = self.number_to_indices[number][0]

            # If index still maps to our target number, return it
            if self.index_to_numbers.get(index) == number:
                return index

            # Otherwise remove this stale index
            heapq.heappop(self.number_to_indices[number])
        return -1
