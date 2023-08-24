"""
Leetcode
68. Text Justification (hard)
2023-08-24

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:

    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
"""

from typing import List


class Solution:
    """
    Runtime: 41 ms, faster than 68.15% of Python3 online submissions for Text Justification.
    Memory Usage: 16.4 MB, less than 69.23% of Python3 online submissions for Text Justification.
    """

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line = []
        line_len = 0

        for word in words:
            if line_len + 1 + len(word) <= maxWidth or not line:
                line.append(word)
                line_len += len(word) + (len(line) > 1)

            else:
                # join current line
                spaces = maxWidth - line_len
                places = len(line) - 1
                if places > 0:
                    for i in range(spaces % places):
                        line[i] += " "
                    ans.append((" " + " " * (spaces // places)).join(line))
                else:
                    ans.append(line[0] + " " * spaces)

                # start a new line
                line = [word]
                line_len = len(word)

        # join the last line
        end_spaces = maxWidth - line_len
        line[-1] += " " * end_spaces
        ans.append(" ".join(line))

        return ans


class Solution1:
    """
    leetcode solution
    Runtime: 43 ms, faster than 55.69% of Python3 online submissions for Text Justification.
    Memory Usage: 16.4 MB, less than 69.23% of Python3 online submissions for Text Justification.
    """

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def get_words(i):
            current_line = []
            curr_length = 0

            while i < len(words) and curr_length + len(words[i]) <= maxWidth:
                current_line.append(words[i])
                curr_length += len(words[i]) + 1
                i += 1

            return current_line

        def create_line(line, i):
            base_length = -1
            for word in line:
                base_length += len(word) + 1

            extra_spaces = maxWidth - base_length

            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces

            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            needs_extra_space = extra_spaces % word_count

            for j in range(needs_extra_space):
                line[j] += " "

            for j in range(word_count):
                line[j] += " " * spaces_per_word

            return " ".join(line)

        ans = []
        i = 0

        while i < len(words):
            current_line = get_words(i)
            i += len(current_line)
            ans.append(create_line(current_line, i))

        return ans


s = Solution()
tests = [
    ((["Listen", "to", "many,", "speak", "to", "a", "few."], 6),
     ["Listen", "to    ", "many, ", "speak ", "to   a", "few.  "]),

    ((["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do", "for", "your", "country"], 16),
     ["ask   not   what",
      "your country can",
      "do  for  you ask",
      "what  you can do",
      "for your country"]),

    ((["This", "is", "an", "example", "of", "text", "justification."], 16),
     [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]),

    ((["What", "must", "be", "acknowledgment", "shall", "be"], 16),
     [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]),

    ((["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20),
     [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]),
]
for inp, exp in tests:
    res = s.fullJustify(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
