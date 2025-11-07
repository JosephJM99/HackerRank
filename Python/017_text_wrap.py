'''
You are given a string and width.
Your task is to wrap the string into a paragraph of width.
'''

# method #1
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
# method #2
string, max_width = input(), int(input())
for x in range(0, len(string), max_width):
    print(string[x:x+max_width])