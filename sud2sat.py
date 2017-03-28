#!/usr/bin/python

import sys


def base9(i, j, k):
    """Convert a number to base 9"""
    return 81 * (i - 1) + 9 * (j - 1) + (k - 1) + 1
# one number per cell rule

def main(input_fname, output_fname):
    row_pos = 1
    col_pos = 1
    rules = ""
    outline = ""
    clause_count = 0

    with open(input_fname, 'r') as in_file:

        for line in in_file:
            if(line[0].isdigit()):
                col_pos = 1
                for char in line:
                    if char != '0' and char != '\n':
                        outline = str(
                            81 * (row_pos - 1) + 9 * (col_pos - 1) + (int(char) - 1) + 1) + " 0" + '\n'
                        rules += outline
                        clause_count = clause_count + 1

                    col_pos = col_pos + 1
                row_pos = row_pos + 1
        print(clause_count)

        # all contain a number rule
        for i in range(81):
            outline = ""
            for j in range(1, 10):
                outline = outline + str(i * 9 + j) + " "
            outline = outline + '0'
            outline = outline + '\n'
            rules += outline
            clause_count = clause_count + 1
        print(clause_count)

        outline = ""
        # once per row rule
        for i in range(1, 10):
            for k in range(1, 10):
                for j in range(1, 9):
                    for l in range((j + 1), 10):
                        outline = str(-base9(i, j, k)) + " " + \
                            str(-base9(i, l, k)) + " 0" + '\n'
                        rules += outline
                        clause_count = clause_count + 1
        print(clause_count)

        outline = ""
        # once per column rule
        for j in range(1, 10):
            for k in range(1, 10):
                for i in range(1, 9):
                    for l in range((i + 1), 10):
                        #    for k in range(1,9):
                        outline = str(-base9(i, j, k)) + " " + \
                            str(-base9(l, j, k)) + " 0" + '\n'
                        rules += outline
                        clause_count = clause_count + 1
        print(clause_count)

        # one 1 per col 1
        #-1 -82
        #-1 -163
        #...
        #-1 -649
        #
        # one 2 per col 1
        #-2 -83
        #...
        #-2 -650
        #
        # one 1 per col 2
        #-10 -91
        #-10 -172
        #...
        #
        # one 9 per col 9
        #-81 -162
        #...
        #-81 -729

        count = 0
        outline = ""
        for k in range(1, 10):
            for a in range(3):
                for b in range(3):
                    for u in range(1, 4):
                        for v in range(1, 3):
                            for w in range((v + 1), 4):
                                i = (3 * a + u)
                                j = (3 * b + v)
                                jp = (3 * b + w)

                                outline = str(-base9(i, j, k)) \
                                    + " " + \
                                    str(-base9(i, jp, k)) + " 0" + '\n'
                                rules += outline
                                count = count + 1
                                clause_count = clause_count + 1
        print(clause_count)

        count = 0
        outline = ""
        for k in range(1, 10):
            for a in range(3):
                for b in range(3):
                    for u in range(1, 3):
                        for v in range(1, 4):
                            for w in range((u + 1), 4):
                                for t in range(1, 4):
                                    i = (3 * a + u)
                                    j = (3 * b + v)
                                    ip = (3 * a + w)
                                    jp = (3 * b + t)

                                    outline = str(-base9(i, j, k)) \
                                        + " " + \
                                        str(-base9(ip, jp, k)) + " 0" + '\n'
                                    rules += outline
                                    count = count + 1
                                    clause_count = clause_count + 1
        print(clause_count)

    with open(output_fname, 'w') as out_file:
        out_file.write("p cnf 729 {0} \n".format(clause_count))
        out_file.write(rules)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: python {0} <input file> <output file>".format(sys.argv[0])
        sys.exit(0)
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    try:
        main(input_file, output_file)
    except KeyboardInterrupt:
        print '\nExiting by user request.\n'
        sys.exit(0)
