#!/bin/bash

set -e

if [ -z "$1" ]
  then
    echo "Usage: $0 <puzzle file>"
    exit 1
fi

# Prep
mkdir -p tmp

echo
echo "==== TESTING: $1 ===="

# Convert to CNF in DIMACS
echo
echo "== TRANSLATING to DIMACS =="
echo "python sud2sat.py $1 tmp/$(basename $1).cnf"
python sud2sat.py $1 tmp/$(basename $1).cnf

# Run SAT solver
echo
echo "== SOLVING: tmp/$(basename $1).cnf =="
echo "minisat tmp/$(basename $1).cnf tmp/$(basename $1).sat"
echo
minisat tmp/$(basename $1).cnf tmp/$(basename $1).sat & wait

# Print solved sudoku
echo
echo "== PARSING SOLUTION =="
echo "python sat2sud.py tmp/$(basename $1).sat"
python sat2sud.py tmp/$(basename $1).sat

