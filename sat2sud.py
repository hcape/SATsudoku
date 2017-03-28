#!/usr/bin/python

from __future__ import print_function
def neg(el):
    return el > 0

def decode(num):
    return 

f = open('ans.txt', 'r')

verts = []
next(f)
for line in f:
    verts.append([int(val) for val in line.split() if int(val) > 0])
#print(verts)
#print(len(verts[0]))


Matrix = [[0 for x in range(9)] for y in range(9)] 

format_count = 1
for num in verts[0]:
    num = num - 1;
    row_mod = divmod(num, 81)
    row_num = row_mod[0]
    col_mod = divmod(row_mod[1], 9)
    col_num = col_mod[0]
    value_in_square = col_mod[1] + 1
    #print(num, row_num, col_num)
    Matrix[row_num][col_num] = value_in_square

print("Solved ________________________")
for i in range(9):
    for j in range(9):
        print( '|' + str(Matrix[i][j]) + '|', end='')
    print('\n')


