'''
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.
'''

def main(c, t):
    for i in range(t):
        print((c*i).rjust(t-1)+c+(c*i).ljust(t-1))
        
    for i in range(t+1):
        print((c*t).center(t*2)+(c*t).center(t*6))
        
    for i in range((t+1)//2):
        print((c*t*5).center(t*6))
        
    for i in range(t+1):
        print((c*t).center(t*2)+(c*t).center(t*6))
        
    for i in range(t):
        print(((c*(t-i-1)).rjust(t)+c+(c*(t-i-1)).ljust(t)).rjust(t*6))
        
        
if __name__ == '__main__':
    c = 'H'
    thickness = int(input())
    main(c, thickness)