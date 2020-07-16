class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        if n == 0:
            return [[]]
        elif n == 1:
            return [[1]]

        left = up = n - 1
        right = down = 0
        x = y = 0
        dx, dy = 1, 0

        i = 2
        ans = [[1 for _ in range(n)] for _ in range(n)]

        while right <= left and down <= up:
            if dx != 0:
                x += dx

                if x == left and dx == 1:
                    dx, dy = 0, 1
                    down += 1
                elif x == right and dx == -1:
                    dx, dy = 0, -1
                    up -= 1
            elif dy != 0:
                y += dy

                if y == down and dy == -1:
                    dx, dy = 1, 0
                    right += 1
                elif y == up and dy == 1:
                    dx, dy = -1, 0
                    left -= 1

            ans[y][x] = i
            i += 1

        return ans

s = Solution()
a = s.generateMatrix(5)

print(a)




        # 1  2  3  4
        # 12 13 14 5
        # 11 16 15 6
        # 10 9  8  7
        