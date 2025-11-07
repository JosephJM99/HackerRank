'''
Consider the following:

A string, s, of length n where s = c0c1...cn-1.
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index < j in ti, then do not include the character in string ui.
Given s and k, print n/k lines where each line i denotes string ui.

Example

s = 'AAABCADDE'
k = 3
'''

from collections import OrderedDict


def merge_the_tools(string, k):
    # method #1
    for i in range(0, len(string), k):
        s = ''
        for ch in string[i : i + k]:
            if ch not in s:
                s += ch
        print(s)
        
    # method #2
    for i in range(0, len(string), k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)