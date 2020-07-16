class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if not rowIndex:
            return [1]

        prevRow = [1]
        for i in range(rowIndex):
            row = [1]
            for j in range(len(prevRow) - 1):
                row.append(prevRow[j] + prevRow[j+1])
            row.append(1)
            prevRow = row

        return prevRow

s = Solution()

print(s.getRow(7))