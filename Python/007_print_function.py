'''
The included code stub will read an integer n, from STDIN.

Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.
'''
def print_func(n):
    for i in range(1, n+1):
        print(i, end='')
        

if __name__ == '__main__':
    n = int(input())
    if n >= 1 and n <= 150:
        print_func(n)