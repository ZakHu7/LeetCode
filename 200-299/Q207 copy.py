from typing import Collection, List
from collections import deque
class Course:
  def __init__(self):
    self.preReq = set()
    self.blocking = set()

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    courses = [None] * numCourses
    for i in range(numCourses):
      courses[i] = Course()
      
    for prerequisite in prerequisites:
      courses[prerequisite[0]].preReq.add(courses[prerequisite[1]])
      courses[prerequisite[1]].blocking.add(courses[prerequisite[0]])
    
    queue = deque()
    for i in range(numCourses):
      if len(courses[i].preReq) == 0:
        queue.append(courses[i])
        
    while queue:
      course = queue.popleft()
      numCourses -= 1
      for blocked in course.blocking:
        blocked.preReq.remove(course)
        if len(blocked.preReq) == 0:
          queue.append(blocked)
    return numCourses == 0
      