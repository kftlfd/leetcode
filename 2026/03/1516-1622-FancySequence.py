"""
Leetcode
2026-03-15
1622. Fancy Sequence
Hard

Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:

    Fancy() Initializes the object with an empty sequence.
    void append(val) Appends an integer val to the end of the sequence.
    void addAll(inc) Increments all existing values in the sequence by an integer inc.
    void multAll(m) Multiplies all existing values in the sequence by an integer m.
    int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.

 

Example 1:

Input
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
Output
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

Explanation
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20

 

Constraints:

    1 <= val, inc, m <= 100
    0 <= idx <= 10^5
    At most 10^5 calls total will be made to append, addAll, multAll, and getIndex.


Hint 1
Use two arrays to save the cumulative multipliers at each time point and cumulative sums adjusted by the current multiplier.
Hint 2
The function getIndex(idx) ask to the current value modulo 10^9+7. Use modular inverse and both arrays to calculate this value.
"""

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)


class Fancy:
    """
    Time Limit Exceeded
    """

    def __init__(self):
        self.nums = []
        self.ops = []
        self.ADD = 0
        self.MULT = 1
        self.MOD = (10**9) + 7

    def append(self, val: int) -> None:
        self.nums.append((val, len(self.ops)))

    def addAll(self, inc: int) -> None:
        self.ops.append((self.ADD, inc))

    def multAll(self, m: int) -> None:
        self.ops.append((self.MULT, m))

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        num, ops_start = self.nums[idx]
        for op, val in self.ops[ops_start:]:
            if op == self.ADD:
                num += val
            else:
                num *= val
        return num % self.MOD


class Fancy1:
    """
    leetcode solution 1: Use modular inverse for the getIndex operation
    Runtime 249ms Beats 29.03%
    Memory 56.36MB Beats 50.00%
    """

    def __init__(self):
        self.mod = 10**9 + 7
        self.v = list()
        self.a = [1]
        self.b = [0]

    # fast exponentiation
    def quickmul(self, x: int, y: int) -> int:
        return pow(x, y, self.mod)

    # multiplicative inverse
    def inv(self, x: int) -> int:
        return self.quickmul(x, self.mod - 2)

    def append(self, val: int) -> None:
        self.v.append(val)
        self.a.append(self.a[-1])
        self.b.append(self.b[-1])

    def addAll(self, inc: int) -> None:
        self.b[-1] = (self.b[-1] + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a[-1] = self.a[-1] * m % self.mod
        self.b[-1] = self.b[-1] * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.v):
            return -1
        ao = self.inv(self.a[idx]) * self.a[-1]
        bo = self.b[-1] - self.b[idx] * ao
        ans = (ao * self.v[idx] + bo) % self.mod
        return ans


class Fancy2:
    """
    leetcode solution 2: Use multiplicative inverse during the append operation
    Runtime 265ms Beats 22.58%
    Memory 54.55MB Beats 87.10%
    """

    def __init__(self):
        self.mod = 10**9 + 7
        self.v = list()
        self.a = 1
        self.b = 0

    # fast exponentiation
    def quickmul(self, x: int, y: int) -> int:
        return pow(x, y, self.mod)

    # multiplicative inverse
    def inv(self, x: int) -> int:
        return self.quickmul(x, self.mod - 2)

    def append(self, val: int) -> None:
        self.v.append((val - self.b) * self.inv(self.a) % self.mod)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a = self.a * m % self.mod
        self.b = self.b * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.v):
            return -1
        return (self.a * self.v[idx] + self.b) % self.mod
