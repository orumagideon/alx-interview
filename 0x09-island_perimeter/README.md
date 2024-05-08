# Island Perimeter

## Task Description
This task involves creating a function `island_perimeter(grid)` that calculates and returns the perimeter of an island described in a grid.

### Specifications
- The `grid` is a list of lists of integers:
  - 0 represents water
  - 1 represents land
- Each cell is square, with a side length of 1 unit.
- Cells are connected horizontally or vertically (not diagonally).
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Files
- `0-island_perimeter.py`: Contains the function `island_perimeter(grid)`.

## Usage
```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
Example Output
$ ./0-main.py
12
Author
orumagideon
