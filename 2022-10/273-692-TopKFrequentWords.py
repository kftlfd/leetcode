"""
Leetcode
692. Top K Frequent Words (medium)
2022-10-19

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
"""

from typing import List, Optional
from collections import Counter


# wrong
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = Counter(words).most_common(k)

        buckets = []
        curr_freq = None
        for word, freq in cnt:
            if not curr_freq or freq != curr_freq:
                buckets.append([word])
                curr_freq = freq
            else:
                buckets[-1].append(word)

        ans = []
        for bucket in buckets:
            if len(bucket) > 1:
                ans += sorted(bucket)
            else:
                ans += bucket

        return ans


# Runtime: 70 ms, faster than 82.18% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 14 MB, less than 64.49% of Python3 online submissions for Top K Frequent Words.
class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(sorted(words)).most_common(k)
        return [pair[0] for pair in cnt]


s = Solution1()
tests = [
    ((['c', 'c', 'a', 'b', 'b'], 2),
     ['b', 'c']),

    ((["i", "love", "leetcode", "i", "love", "coding"], 2),
     ["i", "love"]),

    ((["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
     ["the", "is", "sunny", "day"]),

    ((["i", "love", "leetcode", "i", "love", "coding"], 3),
     ["i", "love", "coding"])
]
for inp, exp in tests:
    words, k = inp
    res = s.topKFrequent(words, k)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
print('Completed testing')
