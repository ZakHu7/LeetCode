from typing import List
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
      return 0
    rowL = len(grid)
    colL = len(grid[0])
    ans = 0
    def dfs(r, c):
      if r < 0 or r >= rowL or c < 0 or c >= colL\
        or grid[r][c] != '1':
        return
      grid[r][c] = '2'
      dfs(r+1, c)
      dfs(r-1, c)
      dfs(r, c+1)
      dfs(r, c-1)
      
    for r in range(rowL):
      for c in range(colL):
        if grid[r][c] == '1':
          ans += 1
          dfs(r, c)
    
    return ans
  