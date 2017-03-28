# SATsudoku

*A SAT solver for sudoku puzzles*

## Getting started

Before running:

```bash
sudo apt install python-minimal -y
```

To solve a puzzle:

1. Update sudoku file with puzzle
2. Run python sud2sat.py
3. Run minisat cnf.txt ans.txt ( with >> stats.txt to accumulated stats)
4. Run python sat2sud.py (with >> solved.txt to accumulated solved grids)

### Files

* `ans.txt` the encoded solution from the `minisat`. Output from `minisat`. File read in `sat2sud`.
* `cnf.txt` -> the encoded rules to input to the `minisat`. Output from `sud2sat`. Input to `minisat`.
* `solved.txt` -> the decoded solved solutions to the sudoku. Output from `sat2sud`.
* `stats.txt` -> Stats from solving the `minisat`. Console output from `minisat`.
* `sudoku.txt` -> Sudoku problem. File read in `sud2sat`.

In the form

```
Grid 50
300200000
000107000
706030500
070009080
900020004
010800050
009040301
000702000
000008006
```

## Todo

### Basic
 * [x] Write translator
 * [ ] Aggregate stats data
 * [ ] Write report
 * [ ] Comment and clean code
 * [ ] Makefile or something

### Advanced

 * [ ] Do hard problems
 * [ ] Try at least one alternate to the minimal encoding (?)
 * [ ] Try another SAT solver
 * [ ] Comparison to special-purpose Sudoku solvers
