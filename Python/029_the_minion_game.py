'''
Kevin and Stuart want to play the 'The Minion Game'.
'''

def minion_game(string):
    s = len(string)
    v = 0
    c = 0
    for i in range(s):
        if string[i] in 'AEIOU':
            v += (s - i)
        else: c += (s - i)
        
    if v < c:
        print('Stuart ' + str(c))
    elif v > c:
        print('Kevin ' + str(v))
    else:
        print('Draw')
        

if __name__ == '__main__':
    s = input()
    minion_game(s)