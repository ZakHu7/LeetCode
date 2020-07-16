class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        d = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            d[prerequisites[i][0]].append(prerequisites[i][1])
        
        complete = [0 for _ in range(numCourses)]
        order = []

        for i in range(numCourses):
            if not self.findOrderH(d, complete, order, i):
                return []

        return order

    def findOrderH(self, d, complete, order, ind):
        if complete[ind] == -1:
            return False
        elif complete[ind] == 0:
            for i in range(len(d[ind])):
                complete[ind] = -1
                if not self.findOrderH(d, complete, order, d[ind][i]):
                    return False

            order.append(ind)
            complete[ind] = 1

        ## if complete[ind] == 1, it has already been added
        return True

s = Solution()
numCourses = 5
prerequisites = [[0,3],[1,3],[3,1],[3,4]]

print(s.findOrder(numCourses, prerequisites))


        
        