"""
Leetcode
1146. Snapshot Array (medium)
2023-06-11

Implement a SnapshotArray that supports the following interface:

    SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
    void set(index, val) sets the element at the given index to be equal to val.
    int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
    int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

Constraints:

    1 <= length <= 5 * 10^4
    0 <= index < length
    0 <= val <= 10^9
    0 <= snap_id < (the total number of times we call snap())
    At most 5 * 10^4 calls will be made to set, snap, and get.
"""

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

import bisect


class SnapshotArray:
    """
    Memory Limit Exceeded
    """

    def __init__(self, length: int):
        self.arr = [0] * length
        self.snaps = {}
        self.next_snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snaps[self.next_snap_id] = self.arr[:]
        self.next_snap_id += 1
        return self.next_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id][index]


class SnapshotArray1:
    """
    leetcode solution
    Runtime: 666 ms, faster than 70.03% of Python3 online submissions for Snapshot Array.
    Memory Usage: 45.6 MB, less than 37.33% of Python3 online submissions for Snapshot Array.
    """

    def __init__(self, length: int):
        self.arr = [[[0, 0]] for _ in range(length)]
        self.id = 0
        self.max_val = 10**9

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.id, val])

    def snap(self) -> int:
        out = self.id
        self.id += 1
        return out

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect(self.arr[index], [snap_id, self.max_val])
        return self.arr[index][snap_index - 1][1]
