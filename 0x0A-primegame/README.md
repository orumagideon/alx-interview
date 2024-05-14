# Prime Game

## Description
Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. They remove the chosen number and its multiples from the set. The player who cannot make a move loses the game. This program determines the winner of each game based on a given number of rounds and different values of n.

## Prototype
```python
def isWinner(x, nums)
x: The number of rounds.
nums: An array of integers representing different values of n for each round.
Return
The name of the player who won the most rounds. If the winner cannot be determined, it returns None.

Constraints
n and x will not be larger than 10000.
No external packages are allowed in the implementa
x = 3
nums = [4, 5, 1]
# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: 1
# Ben wins because there are no prime numbers for Maria to choose

# Result: Ben has the most wins

print(isWinner(3, [4, 5, 1]))  # Output: "Ben"
Usage
./main_0.py

Here's the readme.md file for your Prime Game project:

markdown
Copy code
# Prime Game

## Description
Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. They remove the chosen number and its multiples from the set. The player who cannot make a move loses the game. This program determines the winner of each game based on a given number of rounds and different values of n.

## Prototype
```python
def isWinner(x, nums)
x: The number of rounds.
nums: An array of integers representing different values of n for each round.
Return
The name of the player who won the most rounds. If the winner cannot be determined, it returns None.

Constraints
n and x will not be larger than 10000.
No external packages are allowed in the implementation.
Example
python
Copy code
x = 3
nums = [4, 5, 1]
# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: 1
# Ben wins because there are no prime numbers for Maria to choose

# Result: Ben has the most wins

print(isWinner(3, [4, 5, 1]))  # Output: "Ben"
Usage
bash
Copy code
./main_0.py
Authors orumagideon
