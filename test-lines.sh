#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage: $0 <multiline puzzle file>"
    exit 1
fi

printf "Testing $(basename $1)\n"

mkdir -p tmp/$(basename $1).puzzles
split -d -e -l 1 $1 tmp/$(basename $1).puzzles/

mkdir -p out/$(basename $1).solns/
for file in tmp/$(basename $1).puzzles/*; do
  printf "\rTesting Puzzle #$(basename $file)"
  ./test.sh $file > out/$(basename $1).solns/$(basename $file).soln
done

printf "\nWriting solutions to out/$(basename $1).soln\n"
cat out/$(basename $1).solns/* > out/$(basename $1).soln
