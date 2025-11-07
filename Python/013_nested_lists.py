'''
Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''

if __name__ == '__main__':
    std_info = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        std_info.append([name, score])
    scores = [x[1] for x in std_info]
    min_score_list = sorted(set(scores))
    results = sorted([y[0] for y in std_info if y[1]==min_score_list[1]])
    [print(x) for x in results]