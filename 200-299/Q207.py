class Solution:
    def canFinish(self, numCourses, prerequisites):
        # check all courses to see if they can be completed

        possible = [0 for _ in range(numCourses)]

        allPrereq = [[] for _ in range(numCourses)]

        for item in prerequisites:
            if item[0] == item[1]:
                continue
            allPrereq[item[0]].append(item[1])


        for i in range(numCourses):
            if not self.dfs(i, possible, allPrereq):
                return False

        return True
    
    def dfs(self, pos, possible, allPrereq):
        # if not allPrereq[pos]:
        #     possible[pos] = 1
        #     return True

        if possible[pos] == -1:
            return False
        if possible[pos] == 1:
            return True
        
        possible[pos] = -1
        
        for i in range(len(allPrereq[pos])):
            if not self.dfs(allPrereq[pos][i], possible, allPrereq):
                return False
        
        possible[pos] = 1
        return True
    


s = Solution()

numCourses = 4

prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]
prerequisites2 = [[0,2],[1,2],[2,0]]

print(s.canFinish(numCourses, prerequisites2))
