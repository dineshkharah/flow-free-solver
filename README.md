# Flow Free Solver

Solve Flow Free puzzles from a screenshot. Flow Free is the puzzle known as Numberlink: connect every pair of colored dots and fill every cell, with no pipe crossing or overlapping another.

The tool takes a picture of a board, reads it, solves it, and draws the answer so it can be copied back onto the phone by hand.

## How it is built

The work is split by stage, and each stage gets its own folder when its turn comes. Right now only the solver stage exists:

- `board.py` the shared types every stage agrees on
- `solve/` the puzzle solver and its verifier

Detection, drawing, and screen capture arrive in later steps and get their folders then.

## Running it

There is nothing to run end to end yet.

Install the requirements from the project root:

```
pip install -r requirements.txt
```

Run the tests from the project root:

```
pytest
```
