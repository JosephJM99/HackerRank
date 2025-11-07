'''
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

1. The length of the segment matches Ron's birth month, and,
2. The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

Example
s = [2, 2, 1, 3, 2]
d = 4
m = 2

Lily wants to find segments summing to Ron's birth day, d = 4 with a length equalling his birth month, m = 2. In this case, there are two segments meeting her criteria: [2, 2] and [1, 3].
'''

def birthday(s, d, m):
    x = 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d:
            x += 1
    return x

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)
