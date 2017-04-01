# SATsudoku

*A SAT solver for sudoku puzzles*

### Team Members

| Name         | Student #  |
| ---          | ---        |
| Heather Cape |  V00795197 |
| Brynn Hawker |  V00797467 |
| Boyang Jiao  |  V00800928 |


## Getting started

### Requirements

* Ubuntu 16.04 LTS 64bit
* Python 2.7 (`sudo apt install python-minimal -y`)
* Minisat (`sudo apt install minisat -y`)

You may need to `sudo chmod u+x *.sh` to get the scripts to run.

### Single puzzle file

To solve/test a single puzzle you can use the `test.sh` script

```bash
./test.sh <puzzle file>
```

make sure your puzzle file contains **only a sudoku puzzle** with no extra lines.

### Multiline puzzle file

To solve a set of puzzles from a file you can use the `test-lines.sh` script

```bash
./test-lines.sh <multiline puzzle file>
```

make sure your file has **exactly 1 puzzle per line** and no trailing new line.

The results will be placed in the `out/` directory.

### Manual Testing

If you'd like to manually run a translator you can perform the actions in `test.sh` by hand. For example, to solve the sudoku in `tests/simple.txt`,

```bash
mkdir tmp

# Convert to CNF in DIMACS
python sud2sat.py tests/simple.txt tmp/simple.cnf

# Run SAT solver
minisat tmp/simple.cnf tmp/simple.sat

# Print solved sudoku
python sat2sud.py tmp/simple.sat
```

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
