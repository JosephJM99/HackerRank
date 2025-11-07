'''
Given an integer N, print the following values for each integer i from 1 to N:

Decimal
Octal
Hexadecimal (capitalized)
Binary
'''

# method #1
def print_formatted(number):
    width = len('{0:b}'.format(number))
    for i in range(1, number+1):
        print('{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(i, w=width))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    

# method #2
def formatted(number):
   l = len(bin(number)) - 2
   for i in range(1, number + 1):
      f = ""
      for c in "doXb":
         if f:
            f += " "
         f += "{:>" + str(l) + c + "}"
      print(f.format(i, i, i, i))

n = int(input())
formatted(n)