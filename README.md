# SATsudoku

*A SAT solver for sudoku puzzles*

## Getting started

Before running make sure to

```bash
sudo apt install python-minimal -y
sudo apt install minisat -y
```

To solve/test a single puzzle you can use the `test.sh` script

```bash
./test.sh <puzzle file>
```

make sure your puzzle file **only a sudoku puzzle** with no extra lines.

To solve a set of puzzles from a file you can us the `test-lines.sh` script

```bash
./test-lines.sh <multiline puzzle file>
```

make sure your file has **exactly 1 puzzle per line** and no trailing new line.

## Todo

### Basic
 * [x] Write translator
 * [ ] Aggregate stats data
 * [ ] Write report
 * [ ] Comment and clean code
 * [x] Makefile or something

### Advanced

 * [x] Do hard problems
 * [ ] Try at least one alternate to the minimal encoding (?)
 * [ ] Try another SAT solver
 * [ ] Comparison to special-purpose Sudoku solvers
