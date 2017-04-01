#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage: $0 <multiline puzzle file>"
    exit 1
fi

echo "Splitting $(basename $1)"

mkdir -p tmp/$(basename $1).puzzles
split -d -e -l 1 $1 tmp/$(basename $1).puzzles/

mkdir -p out/$(basename $1).solns/
for file in tmp/$(basename $1).puzzles/*; do
  echo "Testing $file"
  ./test.sh $file > out/$(basename $1).solns/$(basename $file).soln
done

echo "Writing solutions to out/$(basename $1).soln"
cat out/$(basename $1).solns/* > out/$(basename $1).soln
