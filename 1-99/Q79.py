class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        if not board:
            return False

        maxH = len(board)
        maxW = len(board[0])

        def checkMove(x, y):
            if x < 0 or y < 0 or x >= maxW or y >= maxH:
                return False
            return True

        def existH(board, word, wordInd, x, y, soFar):
            if wordInd == len(word):
                return True
            if not checkMove(x, y):
                return False

            let = board[y][x]
            
            if let != word[wordInd]:
                return False

            soFar += let
            
            board[y][x] = ''

            for i in range(-1, 2, 2):
                if existH(board, word, wordInd+1, x+i, y, soFar):
                    return True
                elif existH(board, word, wordInd+1, x, y+i, soFar):
                    return True

            board[y][x] = let

        for i in range(len(board)):
            for j in range(len(board[0])):
                if existH(board, word, 0, j, i, ""):
                    return True

        return False

s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABFCEEE"

print(s.exist(board, word))