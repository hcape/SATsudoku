#!/usr/bin/python

import sys

row_pos = 1;
col_pos = 1;
outline = ""
clause_count = 0
global f


def base9 (i,j,k):
    return (81*(i-1) + 9*(j-1) + (k-1) + 1)
#one number per cell rule

def read():
    global row_pos
    global col_pos
    global outline
    global clause_count
    global f
    
    sud_file = open('sudoku.txt', 'r')
    f = open('temp.txt', 'w')
    for line in sud_file:
        if(line[0].isdigit()):
            col_pos = 1
            for char in line:
                if char != '0' and char != '\n':
                    outline = str(81*(row_pos -1) + 9*(col_pos-1) + (int(char) -1) + 1) + " 0" +'\n'
                    f.write(outline)
                    clause_count = clause_count + 1
                    
                col_pos = col_pos + 1
            row_pos = row_pos + 1   
    print(clause_count)



def read_hard():
    global row_pos
    global col_pos
    global outline
    global clause_count
    global f
    
    sud_file = open('sudoku_hard.txt', 'r')
    f = open('temp_hard.txt', 'w')
    
    #each line is one puzzle
    for line in sud_file:
        col_pos = 1
        for char in line:
            if char != '.' and char != '\n':
                #print(str(81*(row_pos -1) + 9*(col_pos-1) + (int(char) -1) + 1))
                #print("row_pos  = {}, col_pos = {}, char = {}".format(row_pos, col_pos, char))
                
                outline = str(81*(row_pos -1) + 9*(col_pos-1) + (int(char) -1) + 1) + " 0" +'\n'
                f.write(outline)
                clause_count = clause_count + 1


            col_pos = (col_pos % 9) + 1
            if col_pos == 1:
                row_pos = (row_pos % 9 ) + 1


    print(clause_count)


if len(sys.argv) > 1:
    if sys.argv[1] == 'hard':
        # read "hard" format
        read_hard()
    else:
        sys.exit("optional argument 'hard' not found")
else:
    read()



#all contain a number rule
for i in range(81):
    outline=""
    for j in range(1,10):
        outline = outline + str(i*9 + j) + " "
    outline = outline + '0'
    outline = outline + '\n'
    f.write(outline)
    clause_count = clause_count + 1
print(clause_count)
    
outline=""
# once per row rule    
for i in range(1,10):
    for k in range(1,10):
        for j in range(1,9):
            for l in range((j+1), 10):
                outline = str(-base9(i,j,k)) + " "+ str(-base9(i,l,k)) + " 0" +'\n'
                f.write(outline)
                clause_count = clause_count + 1
print(clause_count)


outline=""
#once per column rule
for j in range(1,10):
    for k in range(1,10):
        for i in range (1,9):
            for l in range((i+1), 10):
    #    for k in range(1,9):
                outline = str(-base9(i,j,k)) + " "+ str(-base9(l,j,k)) + " 0" +'\n'
                f.write(outline)
                clause_count = clause_count + 1
print(clause_count)


##one 1 per col 1
#-1 -82
#-1 -163
#...
#-1 -649
#
##one 2 per col 1
#-2 -83
#...
#-2 -650
#
##one 1 per col 2
#-10 -91
#-10 -172
#...
#
##one 9 per col 9
#-81 -162
#...
#-81 -729


count = 0
outline=""
for k in range(1,10):
    for a in range(3):
        for b in range(3):
            for u in range(1,4):
                for v in range(1,3):
                    for w in range((v+1),4):
                        i = (3*a+u)
                        j = (3*b+v)
                        jp =(3*b+w)
                        
                        outline = str(-base9(i,j,k)) \
                                  + " " + \
                                  str(-base9(i,jp,k)) + " 0" + '\n'
                        f.write(outline)
                        count = count +1
                        clause_count = clause_count + 1
print(clause_count)
      
 
count = 0
outline=""
for k in range(1,10):
    for a in range(3):
        for b in range(3):
            for u in range(1,3):
                for v in range(1,4):
                    for w in range((u+1),4):
                        for t in range(1,4):
                            i = (3*a+u)
                            j = (3*b+v)
                            ip =(3*a+w)
                            jp =(3*b+t)

                            outline = str(-base9(i,j,k)) \
                                      + " " + \
                                      str(-base9(ip, jp, k)) + " 0" + '\n'
                            f.write(outline)
                            count = count +1
                            clause_count = clause_count + 1
print(clause_count)
                        

f.close()

if len(sys.argv) > 1:
    if sys.argv[1] == 'hard':
        in_file = open('temp_hard.txt', 'r')
        out_file = open('cnf_hard.txt', 'w')
        
    else:
        sys.exit("optional argument 'hard' not found")
else:
    in_file = open('temp.txt', 'r')
    out_file = open('cnf.txt', 'w')


out_file.write("p cnf 729 " + str(clause_count) + " \n")
for line in in_file:
    out_file.write(line)
in_file.close()
out_file.close()



            



