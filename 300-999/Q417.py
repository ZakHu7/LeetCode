from typing import List
class Solution:
  def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
      return []
    rowLen = len(matrix)
    colLen = len(matrix[0])
    atlantic = [[False] * colLen for _ in range(rowLen)]
    pacific = [[False] * colLen for _ in range(rowLen)]
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    ans = []
    
    def dfs(r, c, visited):
      visited[r][c] = True
      for d in directions:
        newR, newC = r+d[0], c+d[1]
        if newR < 0 or newR >= rowLen or newC < 0 or newC >= colLen \
          or visited[newR][newC] or matrix[newR][newC] < matrix[r][c]:
            continue
        dfs(newR, newC, visited)
      
    for c in range(colLen):
      dfs(0, c, pacific)
      dfs(rowLen-1, c, atlantic)
    for r in range(rowLen):
      dfs(r, 0, pacific)
      dfs(r, colLen-1, atlantic)
    
    for r in range(rowLen):
      for c in range(colLen):
        if atlantic[r][c] and pacific[r][c]:
          ans.append([r,c])
    
    return ans
          
          
s = Solution()
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# matrix = [[3,12,7,6,3,12,17,13,3,9,14,14,3,7,17,8,2,0,19,16,2,14,7,8,7,9,11,2,8,6,14,6,7,12,19],[16,4,0,3,3,6,8,15,19,2,10,17,6,9,12,5,11,12,19,11,15,10,12,8,0,15,11,3,8,1,16,19,16,1,5]]

print(s.pacificAtlantic(matrix))