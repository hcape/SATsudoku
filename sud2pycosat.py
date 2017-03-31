#!/usr/bin/python

import sys, logging
import string
import pycosat

N = 9

# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def base9(i, j, k):
    """Convert a number to base 9"""
    return 81 * (i - 1) + 9 * (j - 1) + (k - 1) + 1
# one number per cell rule

def main(input_fname, output_fname):
    row_pos = 1
    col_pos = 1
    rules = []
    outline = []
    clause_count = 0

    with open(input_fname, 'r') as in_file:

        while True:
            char = '\0'
            col_pos = 1
            while True:
                char = in_file.read(1)
                if char in string.whitespace:
                    continue
                elif char not in '0.*?':
                    outline = [N**2 * (row_pos - 1) + 9 * (col_pos - 1) + (int(char) - 1) + 1]
                    rules.append(outline)
                    clause_count += 1
                logging.debug('%d:%d', row_pos, col_pos)

                col_pos += 1
                if col_pos > 9:
                    break
            row_pos += 1
            if row_pos > 9:
                break
        logging.debug(clause_count)

        # all contain a number rule
        for i in range(N**2):
            outline = []
            for j in range(1, 10):
                outline.append(i * 9 + j)

            rules.append(outline)
            clause_count += 1
        logging.debug(clause_count)

        outline = []
        # once per row rule
        for i in range(1, 10):
            for k in range(1, 10):
                for j in range(1, 9):
                    for l in range((j + 1), 10):
                        outline = [-base9(i, j, k), -base9(i, l, k)]
                        rules.append(outline)
                        clause_count += 1
        logging.debug(clause_count)

        outline = []
        # once per column rule
        for j in range(1, 10):
            for k in range(1, 10):
                for i in range(1, 9):
                    for l in range((i + 1), 10):
                        #    for k in range(1,9):
                        outline = [-base9(i, j, k), -base9(l, j, k)]
                        rules.append(outline)
                        clause_count += 1
        logging.debug(clause_count)

        count = 0
        outline = []
        for k in range(1, 10):
            for a in range(3):
                for b in range(3):
                    for u in range(1, 4):
                        for v in range(1, 3):
                            for w in range((v + 1), 4):
                                i = (3 * a + u)
                                j = (3 * b + v)
                                jp = (3 * b + w)

                                outline = [-base9(i, j, k), -base9(i, jp, k)]
                                rules.append(outline)
                                count = count + 1
                                clause_count += 1
        logging.debug(clause_count)

        count = 0
        outline = []
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

                                    outline = [-base9(i, j, k), -base9(ip, jp, k)]
                                    rules.append(outline)
                                    count = count + 1
                                    clause_count += 1
        logging.debug(clause_count)
    
    with open(output_fname, 'w') as out_file:
        out_file.write( str(pycosat.solve(rules)) )

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print ("Usage: python {0} <input file> <output file>".format(sys.argv[0]))
        sys.exit(0)
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    try:
        main(input_file, output_file)
    except KeyboardInterrupt:
        print ('\nExiting by user request.\n')
        sys.exit(0)
