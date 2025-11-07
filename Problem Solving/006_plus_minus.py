'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
'''

def plusMinus(arr):
    t = len(arr)
    p = len([x for x in arr if x > 0])
    z = len([x for x in arr if x < 0])
    n = len([x for x in arr if x == 0])

    print('{0:.6f}'.format(p/t))
    print('{0:.6f}'.format(z/t))
    print('{0:.6f}'.format(n/t))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
