class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if not numRows:
            return []
        res = [[1]]

        for i in range(1, numRows):
            row = [1]
            for j in range(len(res[-1]) - 1):
                row.append(res[-1][j] + res[-1][j + 1])
            row.append(1)
            res.append(row)

        return res

s = Solution()

print(s.generate(5))
        