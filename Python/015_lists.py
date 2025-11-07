'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''

if __name__ == '__main__':
    items_list = []
    N = int(input())
    for i in range(N):
        items = input().split()
        if len(items)==3:
            eval('items_list.'+items[0]+'('+items[1]+','+items[2]+')')
        elif len(items)==2:
            eval('items_list.'+items[0]+'('+items[1]+')')
        elif items[0]=='print':
            print(items_list)
        else:
            eval('items_list.'+items[0]+'()')