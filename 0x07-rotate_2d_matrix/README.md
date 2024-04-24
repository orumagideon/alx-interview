Rotate 2D Matrix
Task Description
Given an n x n 2D matrix, rotate it 90 degrees clockwise. The rotation should be done in-place, meaning the original matrix is modified.
Prototype
def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (List[List[int]]): The 2D matrix to be rotated.
        
    Returns:
        None
    """
Usage
from 0-rotate_2d_matrix import rotate_2d_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
Output
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
