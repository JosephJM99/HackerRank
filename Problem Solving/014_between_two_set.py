'''
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example
a = [2, 6]
b = [24, 36]

There are two numbers between the arrays: 6 and 12.
6 % 2 == 0, 6 % 6 == 0, 24 % 6 == 0 and 36 % 6 == 0 for the first value.
12 % 2 == 0, 12 % 6 == 0 and 24 % 12 == 0, 36 % 12 == 0 for the second value. Return .
'''

def getTotalX(a, b):
    ans = 0
    for i in range(1, 101):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            ans += 1
    return ans

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    
    total = getTotalX(arr, brr)
    print(total)