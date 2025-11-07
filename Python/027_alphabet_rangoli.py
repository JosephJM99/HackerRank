'''
You are given an integer N. Your task is to print an alphabet rangoli of size N.
'''

# method #1
def print_rangoli(size):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    data = [alpha[i] for i in range(size)]
    items = list(range(size))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
    
# method #2
import string

def print_rangoli(size):
    data = string.ascii_lowercase
    
    li = []
    for i in range(size):
        s = '-'.join(data[i:size])
        li.append((s[::-1]+s[1:]).center(4*n-3, '-'))
    print('\n'.join(li[:0:-1]+li))
        
n = int(input())
print_rangoli(n)