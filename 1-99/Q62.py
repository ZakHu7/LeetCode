class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    row = [1] * n

    for r in range(1, m):
      for c in range(1, n):
        row[c] = row[c] + row[c-1]
    
    return row[-1]

    [1,1,1,1,1,1,1]
    [1,2,3,4,5,6,7]
    [1,3,6,10,15,21,28]