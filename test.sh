#!/bin/bash

set -e

if [ -z "$1" ]
  then
    echo "Usage: $0 <puzzle file>"
    exit 1
fi

# Prep
mkdir -p tmp
mkdir -p out

# Convert to CNF in DIMACS
python sud2sat.py $1 tmp/$(basename $1).cnf

# Run SAT solver
minisat tmp/$(basename $1).cnf tmp/$(basename $1).sat > out/$(basename $1).stats & wait

# Print solved sudoku
python sat2sud.py tmp/$(basename $1).sat | tee out/$(basename $1).ans

