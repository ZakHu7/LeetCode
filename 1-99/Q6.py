class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    rows = [[] for _ in range(numRows)]
    curRow = 0
    direction = 1
    ret = []
    for c in s:
      rows[curRow].append(c)
      curRow += direction
      if curRow == 0 or curRow == numRows-1:
        direction *= -1
    return "".join(["".join(r) for r in rows])


sol = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(sol.convert(s, numRows))