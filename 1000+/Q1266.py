class Solution:
    def minTimeToVisitAllPoints(self, points: [[int]]) -> int:
        ans = 0

        last = points[0]

        for i in range(1, len(points)):
            ans += max(abs(points[i][0] - last[0]), abs(points[i][1] - last[1]))
            last = points[i]

        return ans

s = Solution()
points = [[1,1],[3,4],[-1,0]]

print(s.minTimeToVisitAllPoints(points))