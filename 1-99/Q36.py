from typing import List
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # check row, column and box separately
    for i in range(9):
      if not self.isValidSudokuRow(board, i):
        return False

    for i in range(9):
      if not self.isValidSudokuCol(board, i):
        return False

    for r in [0, 3, 6]:
      for c in [0, 3, 6]:
        if not self.isValidSudokuBox(board, r, c):
          return False
    return True

  def isValidSudokuRow(self, board, i):
    boolList = [False]*9
    for n in board[i]:
      if n != ".":
        if boolList[int(n)-1]:
          return False
        boolList[int(n)-1] = True
    return True

  def isValidSudokuCol(self, board, i):
    boolList = [False]*9
    for r in range(9):
      n = board[r][i]
      if n != ".":
        if boolList[int(n)-1]:
          return False
        boolList[int(n)-1] = True
    return True
    
  def isValidSudokuBox(self, board, r, c):
    boolList = [False]*9
    for i in range(3):
      for j in range(3):
        n = board[r+i][c+j]
        if n != ".":
          if boolList[int(n)-1]:
            return False
          boolList[int(n)-1] = True
    return True


s = Solution()
board = [
["5",".",".",".","7",".",".",".","."]
,["6","5",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

print(s.isValidSudoku(board))