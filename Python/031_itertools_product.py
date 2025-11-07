'''
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
'''

# method #1
from itertools import product


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    
    results = list(product(a, b))
    for x in results:
        print(x, end=' ')
        
        
# method #2
if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    
    results = []
    for i in a:
        for j in b:
            results.append((i, j))
            
    for x in results:
        print(x, end=' ')