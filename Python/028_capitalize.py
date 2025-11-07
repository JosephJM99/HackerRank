'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
'''

# method #1
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
    
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
    
    
# method #2
def solve(s):
    return ' '.join([x[0].upper()+x[1:] for x in s.split()])
    
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
    
    
# method #3
def solve(s):
    return s.title()
    
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)