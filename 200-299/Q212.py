from collections import deque
from typing import List
class TrieNode():
  def __init__(self) -> None:
    self.children = {}
    self.isWord = False


class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    self.makeTrie(words)
    queue = deque()
    res = []
    for word in words:
      if self.findWord(board, word):
        res.append(word)
    return res
  
  def makeTrie
    
  def findWord(self, board, word):
    stack = deque()
    for r in range(len(board)):
      for c in range(len(board[0])):
        visited = set()
        stack.append(((r,c), 0))
        
        while stack:
          cur = stack.pop()
          cRow = cur[0][0]
          cCol = cur[0][1]
          if (cRow, cCol) in visited or cRow < 0 or cRow >= len(board) or cCol < 0 or cCol >= len(board[0]):
            continue
          if board[cRow][cCol] == word[cur[1]]:
            if cur[1] == len(word)-1:
              return True
            visited.add((cRow, cCol))
            stack.append(((cRow-1, cCol), cur[1]+1))
            stack.append(((cRow+1, cCol), cur[1]+1))
            stack.append(((cRow, cCol-1), cur[1]+1))
            stack.append(((cRow, cCol+1), cur[1]+1))
          else:
            visited.remove((cRow, cCol))
    return False
  
s = Solution()
board = [["a","b","c"],
         ["a","e","d"],
         ["a","f","g"]]
words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]

print(s.findWords(board, words))