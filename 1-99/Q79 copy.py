from typing import List
class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    def existH(board, word, index, r, c):
      if r < 0 or r > len(board)-1 or c < 0 or c > len(board[0])-1:
        return False
      res = False
      if board[r][c] == word[index]:
        if index == len(word)-1:
          return True
        val = board[r][c]
        board[r][c] = "-1"
        res = (existH(board, word, index+1, r-1, c)
          or existH(board, word, index+1, r+1, c)
          or existH(board, word, index+1, r, c-1)
          or existH(board, word, index+1, r, c+1))
        board[r][c] = val
      return res

    for r in range(len(board)):
      for c in range(len(board[0])):
        if existH(board, word, 0, r, c):
          return True

    return False