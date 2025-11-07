'''
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
'''

# method #1
if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
    
# method #2
s = input()
li = list(s)

n = a = d = l = u = False
for i in li:
    n = n or i.isalnum()
    a = a or i.isalpha()
    d = d or i.isdigit()
    l = l or i.islower()
    u = u or i.isupper()
    
print(n, a, d, l, u, sep='\n')