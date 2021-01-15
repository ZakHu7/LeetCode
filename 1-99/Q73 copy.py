from typing import List
class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    isFirstRow = False
    isFirstCol = False

    for r in range(len(matrix)):
      for c in range(len(matrix[0])):
        if matrix[r][c] == 0:
          if r == 0:
            isFirstRow = True
          if c == 0:
            isFirstCol = True
          matrix[r][0] = 0
          matrix[0][c] = 0
    
    for r in range(1, len(matrix)):
      if matrix[r][0] == 0:
        for c in range(len(matrix[0])):
          matrix[r][c] = 0

    for c in range(1, len(matrix[0])):
      if matrix[0][c] == 0:
        for r in range(len(matrix)):
          matrix[r][c] = 0

    if isFirstRow:
      for c in range(len(matrix[0])):
        matrix[0][c] = 0
    
    if isFirstCol:
      for r in range(len(matrix)):
        matrix[r][0] = 0
    
      
        