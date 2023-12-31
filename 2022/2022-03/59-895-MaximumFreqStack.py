'''
Leetcode
895. Maximum Frequency Stack (hard)
2022-03-19

Design a stack-like data structure to push elements to the stack and pop 
the most frequent element from the stack.

Implement the FreqStack class:
 - FreqStack() constructs an empty frequency stack.
 - void push(int val) pushes an integer val onto the top of the stack.
 - int pop() removes and returns the most frequent element in the stack.
    - If there is a tie for the most frequent element, the element closest 
      to the stack's top is removed and returned.
'''

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()



# try 1
# Runtime: 4454 ms, faster than 5.04% of Python3 online submissions for Maximum Frequency Stack.
# Memory Usage: 22.5 MB, less than 61.28% of Python3 online submissions for Maximum Frequency Stack.
class FreqStack:

    def __init__(self):
        self.fq = {} # {val: freq}
        self.vals = []
        self.maxfq = -1

        
    def push(self, val: int) -> None:
        self.vals.append(val)
        
        if val not in self.fq.keys(): self.fq[val] = 1
        else: self.fq[val] += 1
        
        self.maxfq = max(self.maxfq, self.fq[val])
        

    def pop(self) -> int:
        out = None
        
        for i in range(len(self.vals) -1, -1, -1):
            if self.fq[self.vals[i]] == self.maxfq:
                out = self.vals[i]
                self.fq[self.vals[i]] -= 1
                self.maxfq = max(self.fq.values())
                del self.vals[i]
                break
                
        return out



# leetcode solution - stack of stacks
# https://leetcode.com/problems/maximum-frequency-stack/solution/
# Runtime: 316 ms, faster than 86.01% of Python3 online submissions for Maximum Frequency Stack.
# Memory Usage: 22.5 MB, less than 70.73% of Python3 online submissions for Maximum Frequency Stack.
import collections
class FreqStackLC:

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(val)

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x



# redone LC solution
# Runtime: 320 ms, faster than 84.21% of Python3 online submissions for Maximum Frequency Stack.
# Memory Usage: 22.4 MB, less than 85.58% of Python3 online submissions for Maximum Frequency Stack.
class FreqStack1:

    def __init__(self):
        self.fqs = {} # freqences
        self.st = {} # stack
        self.maxfq = 0 # max frequence

        
    def push(self, val: int) -> None:
        if val not in self.fqs.keys(): self.fqs[val] = 1
        else: self.fqs[val] += 1

        if self.fqs[val] > self.maxfq: self.maxfq = self.fqs[val]

        if self.maxfq not in self.st.keys(): self.st[self.fqs[val]] = [val]
        else: self.st[self.fqs[val]].append(val)
        

    def pop(self) -> int:
        out = self.st[self.maxfq].pop()
        self.fqs[out] -= 1
        if not self.st[self.maxfq]: self.maxfq -= 1
        return out
        


tests = [
    [ ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
      [[],[5],[7],[5],[7],[4],[5],[],[],[],[]] ],
]
for t in tests:
    print("testing", "\n", t, "\n")
    for i in range(len(t[0])):
        if t[0][i] == "FreqStack":
            fq = FreqStack1()
        elif t[0][i] == "push":
            fq.push(*t[1][i])
        elif t[0][i] == "pop":
            fq.pop(*t[1][i])
