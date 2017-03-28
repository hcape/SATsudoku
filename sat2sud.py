#!/usr/bin/python

import sys

def neg(el):
    return el > 0

def main(input_fname):
    with open(input_fname, 'r') as in_file:

        verts = []
        next(in_file)
        for line in in_file:
            verts.append([int(val) for val in line.split() if int(val) > 0])


        Matrix =  [[0 for x in range(9)] for y in range(9)]

        for num in verts[0]:
            num = num - 1
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
                print '|' + str(Matrix[i][j]) + '|'
            print('\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python {0} <input file>".format(sys.argv[0])
        sys.exit(0)
    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
    try:
        main(input_file)
    except KeyboardInterrupt:
        print '\nExiting by user request.\n'
        sys.exit(0)
